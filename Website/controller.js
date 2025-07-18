angular.module('crudApp', [])
        .controller('CrudController', ['$scope', '$http', function($scope, $http) {
            // Initialize data
            window.MY_SCOPE = $scope;

            $scope.users = [];
            $scope.currentUser = {};
            $scope.isEditing = false;
            $scope.showDeleteModal = false;
            $scope.userToDelete = null;
            $scope.message = {};
            $scope.searchText = '';
            $scope.filteredUsers = [];

            APIrootURL = "http://127.0.0.1:5000";
            
            // Show message function
            $scope.showMessage = function(text, type) {
                $scope.message = {text: text, type: type};
                setTimeout(function() {
                    $scope.$apply(function() {
                        $scope.message = {};
                    });
                }, 3000);
            };
            
            // Create/Update User
            $scope.saveUser = function() {
                if ($scope.userForm.$valid) {
                    if ($scope.isEditing) {
                        // Update existing user
                        $http.put(APIrootURL +'/leads/' + $scope.currentUser.id, $scope.currentUser)
                            .then(function(response) {
                                var index = $scope.users.findIndex(function(u) { return u.id === $scope.currentUser.id; });
                                if (index !== -1) {
                                    $scope.users[index] = angular.copy($scope.currentUser);
                                    $scope.showMessage('User updated successfully!', 'success');
                                }
                                $scope.resetForm();
                            })
                            .catch(function(error) {
                                $scope.showMessage('Error updating user: ' + error.data.error, 'error');
                            });
                    } else {
                        // Add new user
                        $http.post(APIrootURL + '/leads', $scope.currentUser)
                            .then(function(response) {
                                $scope.currentUser.id = response.data.data.id;
                                $scope.users.push(angular.copy($scope.currentUser));
                                $scope.showMessage('User added successfully!', 'success');
                                $scope.resetForm();
                            })
                            .catch(function(error) {
                                $scope.showMessage('Error adding user: ' + error.data.error, 'error');
                            });
                    }
                }
            };
            
            // Edit User
            $scope.editUser = function(user) {
                $scope.currentUser = angular.copy(user);
                $scope.isEditing = true;
                window.scrollTo(0, 0);
            };
            
            // Confirm Delete
            $scope.confirmDelete = function(user) {
                $scope.userToDelete = user;
                $scope.showDeleteModal = true;
            };
            
            // Delete User
            $scope.deleteUser = function() {
                $http.delete(APIrootURL + '/leads/' + $scope.userToDelete.id)
                    .then(function(response) {
                        var index = $scope.users.findIndex(function(u) { return u.id === $scope.userToDelete.id; });
                        if (index !== -1) {
                            $scope.users.splice(index, 1);
                            $scope.showMessage('User deleted successfully!', 'success');
                        }
                        $scope.showDeleteModal = false;
                        $scope.userToDelete = null;
                    })
                    .catch(function(error) {
                        $scope.showMessage('Error deleting user: ' + error.data.error, 'error');
                    });
            };
            
            // Reset Form
            $scope.resetForm = function() {
                $scope.currentUser = {};
                $scope.isEditing = false;
                $scope.userForm.$setPristine();
                $scope.userForm.$setUntouched();
            };
            
            // Gets the user data from the server
            $scope.GetLeads = function() {
                $http.get(APIrootURL + '/leads')
                    .then(function(response) {
                        $scope.usersOBJ = response.data;
                         $scope.usersOBJ.forEach(user => {
                           $scope.users.push( user.value );
                        });
                        $scope.filteredUsers = $scope.users;
                    })
                    .catch(function(error) {
                        $scope.showMessage('Error loading users: ' + error.data.error, 'error');
                    });
            };

            $scope.init = function() {
                $scope.GetLeads();
            }
            
            $scope.init();
        }]);
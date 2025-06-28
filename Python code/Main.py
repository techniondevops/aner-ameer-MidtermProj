# from flask import Flask
import LeadsManager

# app = Flask(__name__)

# @app.route('/', methods=['GET'])
# def index():
#     return LeadsManager.Get()

#this is a test file to check if the code is working

def Main():
    inventory = LeadsManager.Get()
    print("Initial Inventory:", inventory)

    LeadsManager.Add(inventory, {"name":"ori ", "last_name ": "shani","deal-id": 1, "status": "open", "est_value": 100000})
    print("After Adding Item 1:", inventory)

    LeadsManager.Add(inventory, {"name":"yoni ", "last_name ": "golan","deal-id": 2, "status": "close", "est_value": 100000})
    print("After Adding Item 2:", inventory)

    LeadsManager.Update(inventory, 1, {"name":"ori ", "last_name ": "shani"})
    print("After Updating Item 1:", inventory)

    LeadsManager.Remove(inventory, 2)
    print("After Removing Item 2:", inventory)

    LeadsManager.Remove(inventory, 2)
    print("After Removing Item 2 Agian:", inventory)
    
    LeadsManager.Update(inventory, 2,{"name":"yoni ", "last_name ": "golan", "deal-id": 1, "status": "open", "est_value": 100000})
    print("After Updating Item 2 When removed :", inventory)

    

Main()

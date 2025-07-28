import LeadsManager
#this is a test file to check if the code is working


def get_lead_from_user(is_edit=False):
    lead = {}
    lead['name'] = input("Enter lead's name: ") 
    lead['last_name'] = input("Enter lead's last name: ")
    lead['deal-id'] = int(input("Enter lead's deal ID: "))
    lead['is_active'] = LeadsManager.IsDealActive(LeadsManager.Get(), lead['deal-id'])
    lead['est_value'] = int(input("Enter lead's estimated value: ")) 
    return lead

def print_leads(inventory):
    if not inventory:
        print("No leads available.")
        return

    print("\nCurrent Leads:")
    for idx, lead in enumerate(inventory):
        print(f"IDX: {idx}, Name: {lead['name']} {lead['last_name']}, Deal ID: {lead['deal-id']}, Active: {lead['is_active']}, Estimated Value: {lead['est_value']}")
    print("\n")

def Main():
    # inventory = LeadsManager.Get()
    # print("Initial Inventory:", inventory)

    # LeadsManager.Add(inventory, {"name":"ori ", "last_name": "shani","deal-id": 1, "is_active": True, "est_value": 100000})
    # print("After Adding Item 1:", inventory)

    # LeadsManager.Add(inventory, {"name":"yoni ", "last_name": "golan","deal-id": 2, "is_active": False, "est_value": 100000})
    # print("After Adding Item 2:", inventory)

    # LeadsManager.Update(inventory, 0, {"name":"ori ", "last_name": "shani","deal-id": 1, "is_active": True, "est_value": 100000})
    # print("After Updating Item 1:", inventory)

    # LeadsManager.Add(inventory, {"name":"ori ", "last_name": "shani","deal-id": 1, "is_active": True, "est_value": 100000})
    # print("After Adding Item 1:", inventory)

    # LeadsManager.Remove(inventory, 1)
    # print("After Removing Item 2:", inventory)

    # LeadsManager.Update(inventory, 0,{"name":"yoni ", "last_name": "golan", "deal-id": 1, "is_active": True, "est_value": 100000})
    # print("After Updating Item 2 When removed :", inventory)

    # LeadsManager.CloseDeal(inventory, 1)
    # print("After closing deal 1 :", inventory)
    inventory = LeadsManager.Get()

    while True:
        try:
            print("Available commands: list, add, remove, update, close, exit")
            # Get user input
            user_input = input("Enter command (or 'exit' to quit): ").strip().lower()

            match user_input:
                case 'exit':        
                    print("Exiting...")
                    break  

                case 'list':
                    inventory = LeadsManager.Get()   
                    print_leads(inventory)

                case 'add': 
                    LeadsManager.Add(inventory, get_lead_from_user())
                
                case 'remove':
                    id = int(input("Enter the IDX of the lead to remove: "))
                    LeadsManager.Remove(inventory, id)
                
                case 'update':
                    id = int(input("Enter the IDX of the lead to update: "))
                    LeadsManager.Update(inventory, id, get_lead_from_user(True))
                
                case 'close':
                    id = int(input("Enter the ID of the Deal to close: "))
                    LeadsManager.CloseDeal(inventory, id) 
                case _:
                    print("Unknown command. Please try again.")    
        except Exception as e:
            print(f"Error: {e}")

Main()

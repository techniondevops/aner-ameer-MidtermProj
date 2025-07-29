import LeadsManager
#this is a test file to check if the code is working


def get_lead_from_user():
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
                    LeadsManager.Update(inventory, id, get_lead_from_user())
                
                case 'close':
                    id = int(input("Enter the ID of the Deal to close: "))
                    LeadsManager.CloseDeal(inventory, id) 
                case _:
                    print("Unknown command. Please try again.")    
        except Exception as e:
            print(f"Error: {e}")

Main()

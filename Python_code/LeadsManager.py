# inventory = [{ "name": "John Doe", "email": "jone@gmail.com", "phone": "123-456-7890","department": "Sales"}]
inventory = []
def Get():
    return inventory

def Add(inventory , item):
    item['is_active'] = IsDealActive(inventory, item['deal-id'])  # Ensure is_active is set based on deal-id
    # Assign a unique ID to the item
    validate_item(item)
    inventory.append(item) 
    return inventory
    
def Remove(inventory, itemid):
    if itemid < len(inventory) and itemid >= 0:
        inventory.pop(itemid)   
        
    return inventory
    
def Update(inventory, itemid, new_item):
    validate_item(new_item)
    if itemid < len(inventory) and itemid >= 0:
        inventory[itemid] = new_item

    return inventory

def CloseDeal(inventory, itemid):
    for item in inventory:
        if item['deal-id'] == itemid:
            item['is_active'] = False

    return inventory

def IsDealActive(inventory, itemid):
    for item in inventory:
        if item['deal-id'] == itemid:
            return item['is_active']
    
    return True

# def GetActiveDeals(inventory):
#     active_deals = [item for item in inventory if item.get('is_active', False)]
#     return active_deals

def validate_item(item):
    required_fields = ['name', 'last_name', 'deal-id', 'is_active', 'est_value']
    for field in required_fields:
        if field not in item:
            raise ValueError(f"Missing required field: {field}")
    return True
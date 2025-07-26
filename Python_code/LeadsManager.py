# inventory = [{ "name": "John Doe", "email": "jone@gmail.com", "phone": "123-456-7890","department": "Sales"}]
inventory = []
def Get():
    return inventory

def Add(inventory , item):
    # Assign a unique ID to the item
    inventory.append(item) 
    return inventory
    
def Remove(inventory, itemid):
    if itemid < len(inventory) and itemid >= 0:
        inventory.pop(itemid)   
        
    return inventory
    
def Update(inventory, itemid, new_item):
    if itemid < len(inventory) and itemid >= 0:
        inventory[itemid] = new_item

    return inventory

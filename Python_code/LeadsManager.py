idCnt = 0
inventory = {}

def Get():
    return inventory

def Add(inventory , item):
    global idCnt
    idCnt+= 1
    item['id'] = idCnt  # Assign a unique ID to the item
    inventory[idCnt] = item
    return inventory
    
def Remove(inventory, itemid):
    if itemid in inventory:
        inventory.pop(itemid)   
        
    return inventory
    
def Update(inventory, itemid, new_item):
    if itemid in inventory:
        inventory[itemid] = new_item

    return inventory

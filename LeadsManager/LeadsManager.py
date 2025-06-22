idCnt = 0
inventory = {}

def Get():
    return inventory

def Add(inventory , item):
    ++idCnt
    inventory[item[idCnt]] = item
    return inventory
    
def Remove(inventory, itemid):
    inventory.pop(itemid)   
    return inventory
    
def Update(inventory, itemid, new_item):
    inventory[itemid] = new_item
    return inventory

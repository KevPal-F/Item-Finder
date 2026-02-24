from Classes.Equipment import Equipment

dataSource = "Data/Equipment.txt"

def loadEquipment():
    items = []

    with open(dataSource, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts)>=5:
                ID,name,model,description,status = parts
                items.append(Equipment(ID,name,model,description,status))
        return items
    
def saveEquipment(items):
    with open(dataSource, "w") as f:
        for i in items:
            f.write(f"{i.ID},{i.name},{i.model},{i.description},{i.status}\n")

def getEquipment():
    return loadEquipment()

def addEquipment(itemData):
    items = loadEquipment()
    newitem = Equipment(**itemData)
    items.append(newitem)
    saveEquipment(items)
    return newitem

def deleteEquipment(equipmentID):
    items = loadEquipment()
    currItems = [i for i in items if i.ID !=equipmentID]
    success = len(currItems) < len(items)
    if success:
        saveEquipment(currItems)
    return success

def patchEquipment(equipmentID, itemData):
    items = loadEquipment()
    updatedItem = None
    for i in items:
        if i.ID == equipmentID:
            i.name = itemData.get("name", i.name)
            i.model = itemData.get("model", i.model)
            i.description = itemData.get("description", i.description)
            i.status = itemData.get("status", i.status)
            updatedItem = i

    saveEquipment(items)
    return updatedItem
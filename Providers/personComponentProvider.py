from Classes.PersonComponent import PersonComponent

dataSource = "Data/PersonComponent.txt"

def loadPersonComponent():
    own = []

    with open(dataSource, "r") as f:
        lines = f.readlines()
        for line in lines:
            link = line.strip().split(",")
            if len(link) >= 2:
                personID,equipmentID = link
                own.append(PersonComponent(personID,equipmentID))
        return own

def savePersonComponent(own):
    with open(dataSource, "w") as f:
        for o in own:
            f.write(f"{o.personID},{o.equipmentID}\n")

def getPersonComponent(personID):
    own = loadPersonComponent()
    personOwn = [o for o in loadPersonComponent() if o.personID == personID]
    return personOwn

def addPersonComponent(ownData):
    own = loadPersonComponent()
    newOwn = PersonComponent(**ownData)
    own.append(newOwn)
    savePersonComponent(own)
    return newOwn

def deletePersonComponent(personID, equipmentID):
    own = loadPersonComponent()
    currOwn = [o for o in own if (o.personID != personID or o.equipmentID != equipmentID)]
    success = len(currOwn) < len(own)
    if success:
        savePersonComponent(currOwn)
    return success
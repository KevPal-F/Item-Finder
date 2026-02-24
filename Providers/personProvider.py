from Classes.Person import Person

dataSource = "Data/Person.txt"

def loadPeople():
    people = []
    
    with open(dataSource, "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.strip().split(",")
            if len(parts) >= 5:
                ID, name, email, phone, status = parts
                people.append(Person(ID, name, email, phone, status))
        return people
    
def savePeople(people):
    with open(dataSource, "w") as f:
        for p in people:
            f.write(f"{p.ID},{p.name},{p.email},{p.phone},{p.status}\n")

def getPeople():
    return loadPeople()

def addPerson(personData):
    people = loadPeople()
    newPerson = Person(**personData)
    people.append(newPerson)
    savePeople(people)
    return newPerson

def deletePerson(personID):
    people = loadPeople()
    currentPeople = [p for p in people if p.ID != personID]
    success = len(currentPeople) < len(people)
    if success:
        savePeople(currentPeople)
    return success

def patchPerson(personID, personData):
    people = loadPeople()
    updatedPerson = None
    for p in people:
        if p.ID == personID:
            p.name = personData.get("name", p.name)
            p.email = personData.get("email", p.email)
            p.phone = personData.get("phone", p.phone)
            p.status = personData.get("status", p.status)
            updatedPerson = p

    savePeople(people)
    return updatedPerson


class PersonComponent():
    def __init__(self,personID,equipmentID):
        self.personID = personID
        self.equipmentID = equipmentID

    def to_dict(self):
        return {
            "personID":self.personID,
            "equipmentID":self.equipmentID
        }
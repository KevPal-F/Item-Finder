#id, name, description, status, model
class Equipment():
    def __init__(self, ID, name, model, description, status):
        self.ID = ID
        self.name = name
        self.model = model
        self.description = description
        self.status = status

    def __repr__(self):
        return f"{self.ID} {self.name} {self.model} {self.description} {self.status}"

    def to_dict(self):
        return{
            "ID": self.ID,
            "name": self.name,
            "model": self.model,
            "description": self.description,
            "status": self.status,
        }
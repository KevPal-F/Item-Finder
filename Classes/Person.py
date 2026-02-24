#add attribute available
class Person():
    def __init__(self, ID, name, email, phone, status):
        self.ID = ID
        self.name = name
        self.email = email
        self.phone = phone
        self.status = status
    
    def __repr__(self):
        return f"{self.ID} {self.name} {self.email} {self.phone}"
    
    def to_dict(self):
        return{
            "ID": self.ID,
            "name": self.name,
            "email": self.email,
            "phone": self.phone,
            "status": self.status
        }
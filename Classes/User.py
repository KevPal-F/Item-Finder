class User():
    def __init__(self, userID, username, pwd):
        self.userID = userID
        self.username = username
        self.pwd = pwd

    def to_dict(self):
        return{
            "userID": self.userID,
            "username": self.username,
            "password": self.pwd
        }

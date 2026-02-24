from Classes.User import User

dataSource = "Data/Users.txt"

def loadUsers():
    users = []

    with open(dataSource, "r") as f:
        lines = f.readlines()
        for line in lines:
            user = line.strip().split(",")
            if len(user) >= 3:
                userID,username,pwd = user
                users.append(User(userID,username,pwd))
        return users
    
def saveUsers(users):
    with open(dataSource, "w") as f:
        for u in users:
            f.write(f"{u.userID},{u.username},{u.pwd}\n")

def getUser():
    return loadUsers()

def getUsername():
    user = loadUsers()
    usernames = [u for u in user]
    return
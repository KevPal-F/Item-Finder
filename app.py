from flask import Flask
from Controllers.personController import personBP
from Controllers.equipmentController import equipmentBP
from Controllers.personComponentController import personComponentBP

app = Flask(__name__)
app.register_blueprint(personBP)
app.register_blueprint(equipmentBP)
app.register_blueprint(personComponentBP)



if __name__ == "__main__":
    app.run(debug=True)
from flask import Blueprint, jsonify, request
from Providers import personComponentProvider

personComponentBP = Blueprint("personComponentBP", __name__)

@personComponentBP.route("/personComponent/<personID>", methods = ["GET"])
def getPersonComponent(personID):
    personComponent = personComponentProvider.getPersonComponent(personID)
    return jsonify([o.to_dict() for o in personComponent])

@personComponentBP.route("/personComponent", methods = ["POST"])
def addPersonComponent():
    data = request.get_json()
    if not data or "personID" not in data or "equipmentID" not in data:
        return jsonify({"error":"Missing personID or equipmentID"})
    
    personComponent = personComponentProvider.addPersonComponent(data)
    return jsonify(personComponent.to_dict())

@personComponentBP.route("/personComponent/<personID>/<equipmentID>", methods = ["DELETE"])
def deletePersonComponent(personID, equipmentID):
    success = personComponentProvider.deletePersonComponent(personID, equipmentID)
    if success:
        return jsonify({"message":f"Equipment with ID {equipmentID} owned by Person with ID {personID} deleted"})
    return jsonify({"error":f"Equipment with ID {equipmentID} owned by Person with ID {personID} not found"})
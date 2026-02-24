from flask import Blueprint, jsonify, request
from Providers import personProvider

personBP = Blueprint("personBP", __name__)

@personBP.route("/people", methods = ["GET"])
def getPeople():
    people = personProvider.getPeople()
    return jsonify([p.to_dict() for p in people])

@personBP.route("/people", methods = ["POST"])
def addPerson():
    data = request.get_json()
    if not data or "ID" not in data or "name" not in data or "email" not in data or "phone" not in data or "status" not in data:
        return jsonify({"error":"Missing ID, name, email, phone or status"})
    
    person = personProvider.addPerson(data)
    return jsonify(person.to_dict())

@personBP.route("/people/<personID>", methods = ["DELETE"])
def deletePerson(personID):
    success = personProvider.deletePerson(personID)
    if success:
        return jsonify({"message":f"Person {personID} deleted"})
    return jsonify({"error":f"Person with ID {personID} not found"})

@personBP.route("/people/<personID>", methods = ["PATCH"])
def updatePerson(personID):
    data = request.get_json()
    updatedPerson = personProvider.patchPerson(personID, data)
    if updatedPerson:
        return jsonify(updatedPerson.to_dict())
    return jsonify({"error":f"Person with ID {personID} not found"})
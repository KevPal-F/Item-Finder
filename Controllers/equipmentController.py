from flask import Blueprint, jsonify, request
from Providers import equipmentProvider

equipmentBP = Blueprint("equipmentBP", __name__)

@equipmentBP.route("/equipment", methods = ["GET"])
def getEquipment():
    equipment = equipmentProvider.getEquipment()
    return jsonify([e.to_dict() for e in equipment])

@equipmentBP.route("/equipment", methods = ["POST"])
def addEquipment():
    data = request.get_json()
    if not data or "ID" not in data or "name" not in data or "model" not in data or "description" not in data or "status" not in data:
        return jsonify({"error":"Missing ID, name, model, description or status"})
    
    equipment = equipmentProvider.addEquipment(data)
    return jsonify(equipment.to_dict())

@equipmentBP.route("/equipment/<equipmentID>", methods = ["DELETE"])
def deleteEquipment(equipmentID):
    success = equipmentProvider.deleteEquipment(equipmentID)
    if success:
        return jsonify({"message":f"Equipment {equipmentID} deleted"})
    return jsonify({"error":f"Equimpent with ID {equipmentID} not found"})

@equipmentBP.route("/equipment/<equipmentID>", methods = ["PATCH"])
def updateEquipment(equipmentID):
    data = request.get_json()
    updatedEquipment = equipmentProvider.patchEquipment(equipmentID, data)
    if updatedEquipment:
        return jsonify([updatedEquipment.to_dict()])
    return jsonify({"error":f"Equipment with ID {equipmentID} not found"})
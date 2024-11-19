from flask import Blueprint, request, jsonify
from db_setup import db
from models import Vehicle
from schemas import vehicle_schema, vehicles_schema
from marshmallow import ValidationError

routes = Blueprint('routes', __name__)

# Create a vehicle
@routes.route('/vehicle', methods=['POST'])
def create_vehicle():
    try:
        data = request.json
        new_vehicle = vehicle_schema.load(data, session=db.session)
        db.session.add(new_vehicle)
        db.session.commit()
        return jsonify(vehicle_schema.dump(new_vehicle)), 201
    except ValidationError as err:
        return jsonify(err.messages), 422

# Get all vehicles
@routes.route('/vehicle', methods=['GET'])
def get_vehicles():
    vehicles = Vehicle.query.all()
    return jsonify(vehicles_schema.dump(vehicles)) 

# Get a vehicle by VIN
@routes.route('/vehicle/<vin>', methods=['GET'])
def get_vehicle(vin):
    vehicle = Vehicle.query.get(vin)
    if vehicle:
        return jsonify(vehicle_schema.dump(vehicle))
    return jsonify({"error": "Vehicle not found"}), 404

# Update a vehicle
@routes.route('/vehicle/<vin>', methods=['PUT'])
def update_vehicle(vin):
    vehicle = Vehicle.query.get(vin)
    if not vehicle:
        return jsonify({"error": "Vehicle not found"}), 404

    data = request.json
    for key, value in data.items():
        setattr(vehicle, key, value)
    db.session.commit()
    return jsonify(vehicle_schema.dump(vehicle))

# Delete a vehicle
@routes.route('/vehicle/<vin>', methods=['DELETE'])
def delete_vehicle(vin):
    vehicle = Vehicle.query.get(vin)
    if vehicle:
        db.session.delete(vehicle)
        db.session.commit()
        return '', 204
    return jsonify({"error": "Vehicle not found"}), 404

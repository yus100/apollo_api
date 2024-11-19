from db_setup import db
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy import event

class Vehicle(db.Model):
    __tablename__ = 'vehicles'

    vin = db.Column(db.String, primary_key=True, unique=True, index=True)
    manufacturer_name = db.Column(db.String, nullable=False)
    description = db.Column(db.Text)
    horse_power = db.Column(db.Integer, nullable=False)
    model_name = db.Column(db.String, nullable=False)
    model_year = db.Column(db.Integer, nullable=False)
    purchase_price = db.Column(db.Float, nullable=False)
    fuel_type = db.Column(db.String, nullable=False)

    @staticmethod
    def normalize_vin(mapper, connection, target):
        target.vin = target.vin.lower()

# Attach the normalization hook to the Vehicle model
event.listen(Vehicle, 'before_insert', Vehicle.normalize_vin)
event.listen(Vehicle, 'before_update', Vehicle.normalize_vin)

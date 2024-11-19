from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
from models import Vehicle

class VehicleSchema(SQLAlchemySchema):
    class Meta:
        model = Vehicle
        load_instance = True

    vin = auto_field()
    manufacturer_name = auto_field()
    description = auto_field()
    horse_power = auto_field()
    model_name = auto_field()
    model_year = auto_field()
    purchase_price = auto_field()
    fuel_type = auto_field()

vehicle_schema = VehicleSchema()
vehicles_schema = VehicleSchema(many=True)

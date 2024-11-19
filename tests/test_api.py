import unittest
from app import create_app
from db_setup import db

class APITestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.app.config['TESTING'] = True

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.drop_all()

    def test_create_vehicle(self):
        response = self.client.post('/vehicle', json={
            "vin": "12345ABC",
            "manufacturer_name": "Tesla",
            "description": "Electric car",
            "horse_power": 670,
            "model_name": "Model S",
            "model_year": 2022,
            "purchase_price": 79999.99,
            "fuel_type": "Electric"
        })
        self.assertEqual(response.status_code, 201)
        json_data = response.get_json()
        self.assertEqual(json_data['vin'], "12345ABC")
        self.assertEqual(json_data['manufacturer_name'], "Tesla")

    def test_get_all_vehicles(self):
        # First create a vehicle
        self.client.post('/vehicle', json={
            "vin": "12345ABC",
            "manufacturer_name": "Tesla",
            "description": "Electric car",
            "horse_power": 670,
            "model_name": "Model S",
            "model_year": 2022,
            "purchase_price": 79999.99,
            "fuel_type": "Electric"
        })
        response = self.client.get('/vehicle')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(len(json_data), 1)
        self.assertEqual(json_data[0]['vin'], "12345ABC")

    def test_get_vehicle_by_vin(self):
        # First create a vehicle
        self.client.post('/vehicle', json={
            "vin": "12345ABC",
            "manufacturer_name": "Tesla",
            "description": "Electric car",
            "horse_power": 670,
            "model_name": "Model S",
            "model_year": 2022,
            "purchase_price": 79999.99,
            "fuel_type": "Electric"
        })
        response = self.client.get('/vehicle/12345ABC')
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['vin'], "12345ABC")
        self.assertEqual(json_data['model_name'], "Model S")

    def test_update_vehicle(self):
        # Create a vehicle
        self.client.post('/vehicle', json={
            "vin": "12345ABC",
            "manufacturer_name": "Tesla",
            "description": "Electric car",
            "horse_power": 670,
            "model_name": "Model S",
            "model_year": 2022,
            "purchase_price": 79999.99,
            "fuel_type": "Electric"
        })
        # Update the vehicle
        response = self.client.put('/vehicle/12345ABC', json={
            "manufacturer_name": "Tesla Updated",
            "description": "Updated description",
            "horse_power": 680,
            "model_name": "Model S Updated",
            "model_year": 2023,
            "purchase_price": 82999.99,
            "fuel_type": "Electric Updated"
        })
        self.assertEqual(response.status_code, 200)
        json_data = response.get_json()
        self.assertEqual(json_data['manufacturer_name'], "Tesla Updated")
        self.assertEqual(json_data['model_year'], 2023)

    def test_delete_vehicle(self):
        #Create a vehicle
        self.client.post('/vehicle', json={
            "vin": "12345ABC",
            "manufacturer_name": "Tesla",
            "description": "Electric car",
            "horse_power": 670,
            "model_name": "Model S",
            "model_year": 2022,
            "purchase_price": 79999.99,
            "fuel_type": "Electric"
        })

        #Delte the vehicle
        response = self.client.delete('/vehicle/12345ABC')
        self.assertEqual(response.status_code, 204)

        response = self.client.get('/vehicle/12345ABC')
        self.assertEqual(response.status_code, 404)

    def test_create_vehicle_with_invalid_data(self):
        # Test with missing required fields
        response = self.client.post('/vehicle', json={
            "manufacturer_name": "Tesla",
            "description": "Electric car"
        })
        self.assertEqual(response.status_code, 422)

    def test_update_nonexistent_vehicle(self):
        # Attempt to update a vehicle that doesn't exist
        response = self.client.put('/vehicle/99999XYZ', json={
            "manufacturer_name": "Nonexistent",
            "description": "This vehicle does not exist",
            "horse_power": 0,
            "model_name": "None",
            "model_year": 2000,
            "purchase_price": 0.0,
            "fuel_type": "None"
        })
        self.assertEqual(response.status_code, 404)

    def test_delete_nonexistent_vehicle(self):
        # Attempt to delete a vehicle that doesn't exist
        response = self.client.delete('/vehicle/99999XYZ')
        self.assertEqual(response.status_code, 404)

    def test_case_insensitive_vin(self):
        # Create vehicle w uppercase
        response = self.client.post('/vehicle', json={
            "vin": "ABC123",
            "manufacturer_name": "Tesla",
            "description": "Electric car",
            "horse_power": 670,
            "model_name": "Model S",
            "model_year": 2022,
            "purchase_price": 79999.99,
            "fuel_type": "Electric"
        })
        self.assertEqual(response.status_code, 201)  # Vehicle should be created successfully

        # same VIN in lowercase
        response = self.client.post('/vehicle', json={
            "vin": "abc123",
            "manufacturer_name": "Ford",
            "description": "Hybrid car",
            "horse_power": 300,
            "model_name": "Mustang",
            "model_year": 2023,
            "purchase_price": 55999.99,
            "fuel_type": "Hybrid"
        })
        self.assertEqual(response.status_code, 422)  # Expect validation failure
        json_data = response.get_json()
        self.assertIn('vin', json_data)  # contains "vin"
        self.assertIn('already exists', json_data['vin'][0].lower())  # Check for the uniqueness error


if __name__ == '__main__':
    unittest.main()

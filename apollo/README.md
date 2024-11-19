# **Vehicle Management API**

A simple Flask-based web service that provides CRUD-style API access to manage vehicle data stored in a database.

## **Features**

- **CRUD Operations**:
  - **Create**: Add new vehicle records.
  - **Read**: Retrieve all vehicles or a specific vehicle by VIN.
  - **Update**: Modify existing vehicle records.
  - **Delete**: Remove vehicle records by VIN.
- Enforces **case-insensitive uniqueness** on VINs.
- Validates input data using **Marshmallow** schemas.

## **Endpoints**

| Method | URI                   | Description                |
|--------|-----------------------|----------------------------|
| `GET`  | `/vehicle`            | Retrieve all vehicles      |
| `POST` | `/vehicle`            | Create a new vehicle       |
| `GET`  | `/vehicle/<vin>`      | Retrieve a vehicle by VIN  |
| `PUT`  | `/vehicle/<vin>`      | Update a vehicle by VIN    |
| `DELETE` | `/vehicle/<vin>`    | Delete a vehicle by VIN    |

## **Setup Instructions**

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/vehicle-management-api.git
   cd vehicle-management-api
   ```

2. Create a virtual environment and activate it:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the server:
   ```bash
   python app.py
   ```

5. Access the API at `http://127.0.0.1:5000/`.

## **Testing**

Run the test suite to ensure everything works as expected:
```bash
python -m unittest discover tests
```

## **Example Requests**

### **Create a Vehicle**
`POST /vehicle`
```json
{
  "vin": "12345ABC",
  "manufacturer_name": "Tesla",
  "description": "Electric car",
  "horse_power": 670,
  "model_name": "Model S",
  "model_year": 2022,
  "purchase_price": 79999.99,
  "fuel_type": "Electric"
}
```

### **Get All Vehicles**
`GET /vehicle`

### **Update a Vehicle**
`PUT /vehicle/12345ABC`
```json
{
  "manufacturer_name": "Tesla Updated",
  "description": "Updated description",
  "horse_power": 680,
  "model_name": "Model S Updated",
  "model_year": 2023,
  "purchase_price": 82999.99,
  "fuel_type": "Electric Updated"
}
```

### **Delete a Vehicle**
`DELETE /vehicle/12345ABC`

## **Technologies Used**

- **Flask**: Web framework.
- **SQLAlchemy**: ORM for database interactions.
- **Marshmallow**: Validation and serialization.
- **SQLite**: Lightweight database for development.

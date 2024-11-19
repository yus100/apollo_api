from flask import Flask
from config import Config
from db_setup import db
from routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize plugins
    db.init_app(app)

    # Register Blueprints
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)

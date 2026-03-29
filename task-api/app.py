from flask import Flask
from config import Config
from models import db
from routes import task_bp

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)
    app.config.from_object(Config)

    # Setup the database with the app
    db.init_app(app)

    # Register the routes from routes.py
    app.register_blueprint(task_bp)
    
    # Create the database tables before first request if they don't exist
    with app.app_context():
        db.create_all()
        
    return app

if __name__ == '__main__':
    app = create_app()
    # Run the server on port 5000 and enable debug mode
    app.run(debug=True, port=5000)

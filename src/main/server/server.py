from flask import Flask
from flask_cors import CORS
from src.main.routes.events_route import event_route_bp
from src.models.settings.connection import db_connection_handler
from src.main.routes.attendees_route import attendees_route_bp


db_connection_handler.connector_db()

app = Flask(__name__)
CORS(app)

app.register_blueprint(event_route_bp)
app.register_blueprint(attendees_route_bp)
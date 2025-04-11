from flask import Blueprint, jsonify
from services.events import get_next_event

events_blueprint = Blueprint("events", __name__)

@events_blueprint.route("/next", methods=["GET"])
def next_event():
    event = get_next_event()
    if event:
        return jsonify(event), 200
    return jsonify({"message": "No upcoming events found."}), 404
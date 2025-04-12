from flask import Blueprint, jsonify
from services.standings import get_driver_standings
from services.standings import get_constructor_standings

standings_blueprint = Blueprint("standings", __name__)
# drivers_standings_blueprint = Blueprint("drivers_standings", __name__)
# constructors_standings_blueprint = Blueprint("constructors_standings", __name__)


@standings_blueprint.route("/drivers", methods=["GET"])
def get_drivers_standings():
    standings = get_driver_standings()
    if standings:
        return jsonify(standings), 200
    return jsonify({"message": "No standings found."}), 404

@standings_blueprint.route("/constructors", methods=["GET"])
def get_constructors_standings():
    standings = get_constructor_standings()
    if standings:
        return jsonify(standings), 200
    return jsonify({"message": "No standings found."}), 404
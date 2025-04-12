from flask import Flask
from routes.events import events_blueprint
from routes.standings import standings_blueprint

app = Flask(__name__)

# Register blueprints
app.register_blueprint(events_blueprint, url_prefix="/events")
app.register_blueprint(standings_blueprint, url_prefix="/standings")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
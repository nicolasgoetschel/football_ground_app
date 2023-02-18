from flask import Flask, render_template
from controllers.country_controller import countries_blueprint
from controllers.league_controller import leagues_blueprint
from controllers.football_ground_controller import football_grounds_blueprint

app = Flask(__name__)

app.register_blueprint(countries_blueprint)
app.register_blueprint(leagues_blueprint)
app.register_blueprint(football_grounds_blueprint)


if __name__ == '__main__':
    app.run(debug=True)
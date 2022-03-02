from flask import Flask
from Home import h_blueprint
from Signup import signup_blueprint
from flask_cors import CORS
from Saved_stories import saved_blueprint

application = Flask(__name__)
CORS(application, resources={
    f'/*'
})

@application.route("/")
def starting_url():
	return "Homepage to the News Aggregator Api", 200

application.register_blueprint(h_blueprint, url_prefix="/api")
application.register_blueprint(signup_blueprint, url_prefix="/api")
application.register_blueprint(saved_blueprint, url_prefix="/api/save")

if __name__ == '__main__':
    application.run(debug=True)
from flask import Flask, Response
from Home import h_blueprint
from Signup import signup_blueprint
from flask_cors import CORS
from Saved_stories import saved_blueprint


application = Flask(__name__)
cors = CORS(application)
application.config['CORS_HEADERS'] = 'Content-Type'


@application.route("/") 
def starting_url():
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    return 'Homepage', 200


application.register_blueprint(h_blueprint, url_prefix="/api")
application.register_blueprint(signup_blueprint, url_prefix="/api")
application.register_blueprint(saved_blueprint, url_prefix="/api/save")

if __name__ == '__main__':
    application.run(debug=True)

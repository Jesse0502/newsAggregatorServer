from flask import Blueprint, request, Response
from Database import db 

saved_blueprint = Blueprint("saved_stories", __name__)

@saved_blueprint.route("", methods=["GET"])
def getSavedStories():
  response = Response()
  response.headers['Access-Control-Allow-Origin'] = '*'
  userId = request.args['id']
  coll = db['users']
  savedStories = coll.find_one({"_id": userId})
  return {"Data": savedStories['Saved']}, 200

@saved_blueprint.route("", methods=["POST"])
def postSavedStories():
  response = Response()
  response.headers['Access-Control-Allow-Origin'] = '*'
  data = request.json
  userId = request.args['id']
  coll = db['users']
  save_dat = {
    "Heading": data["data"]["heading"],
    "Link": data["data"]["link"],
    "Image": data["data"]["image"],
    "Source": data["data"]["source"],
    "Time": data["data"]["time"]
  }
  coll.find_one_and_update({"_id": userId}, {'$push': {
    'Saved': {
      "$each": [save_dat],
      "$position": 0
    }}
  })
  return "Success", 200
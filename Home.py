from flask import Blueprint, request, Response
import json
from search_query import getSearch
from top_headlines import getTopheadlines, getTopics

h_blueprint = Blueprint("home", __name__)

@h_blueprint.route("", methods=["GET"])
def home():
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    countryCode = request.args['cc']
    query = request.args['q']
    print(countryCode)
    if "topics" in query: 
        res = getTopics(query, countryCode)
        return json.dumps(res)
    elif 'topstories' in query: 
        res = getTopheadlines(query, countryCode)
        return json.dumps(res), 200


@h_blueprint.route("/search", methods=["GET"])
def search():
    response = Response()
    response.headers['Access-Control-Allow-Origin'] = '*'
    countryCode = request.args['cc']
    query = request.args['q']
    limit = request.args['lim']
    res = getSearch(query,countryCode, int(limit))
    print("res len",len(res))
    return json.dumps(res), 200
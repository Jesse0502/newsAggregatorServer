from flask import Blueprint, request
import json 
from jose import jwt
from Database import db
import bcrypt
import python_avatars as pa
import base64
from uuid import uuid4 

signup_blueprint = Blueprint("signup", __name__)

@signup_blueprint.route("/signup", methods=["POST"])
def signup():
    form_data = request.json 
    data = form_data['data'] 
    coll = db['users']
    findUser = coll.find_one({"Email": data['Email']})
    print(findUser)
    if findUser == None:
        hash_password = bcrypt.hashpw(data['Password'].encode('utf8'), bcrypt.gensalt(10))
        gen_avatar = pa.Avatar.random()
        gen_avatar.render("my_avatar.svg")
        with open("my_avatar.svg", 'rb') as image_file:
            encoded_string= base64.b64encode(image_file.read())
            uniqueId = str(uuid4()).replace("-", "")
        coll.insert_one({"_id": uniqueId,"Name": data['Name'], "Email": data["Email"], "Password": hash_password, "Avatar": encoded_string, "Saved": []})
        return {"msg": "User Added Succesfully"}, 200
    
    return {"msg": "User Already exists"}, 200
    
@signup_blueprint.route("/login", methods=["POST"])
def login():
    form_data = request.json
    data = form_data['data']
    coll = db['users']
    findUser = coll.find_one({"Email": data['Email']})
    password = data["Password"]
 
    if findUser != None: 
        compare_passs = bcrypt.checkpw(password.encode('utf8'), findUser["Password"])
        
        if compare_passs == True:
            token = jwt.encode(
            {    
                'id': findUser['_id'],
                'name': findUser['Name'],
                'email': findUser['Email'],
                'avatar': (findUser["Avatar"]).decode('utf-8'),
            }    
                , "secret123")
            
            return {"Token":token}, 200
        else:
            return "Either Email or password is incorrect", 200
    return "No existing user found", 200
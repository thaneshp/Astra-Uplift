import uuid

import bcrypt
from flask import Blueprint, request, session

from dbconnection import db_connect

db_object = db_connect()
global db
db = db_object.apiscan

auth_bp = Blueprint("auth", __name__)


# Function to create a new user
@auth_bp.route("/register/", methods=["POST"])
def create_user():
    content = request.get_json()

    user_id = uuid.uuid4().hex
    name = content["name"]
    email = content["email"]
    password = content["password"].encode("utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())

    try:
        db.users.insert_one(
            {
                "user_id": user_id,
                "fullname": name,
                "email": email,
                "password": hashed_password,
            }
        )

        # Store user_id in session
        session["user_id"] = user_id

        return "User created successfully"
    except:
        print("Failed to update DB")


# # Function for user to login
# @auth_bp.route("/login/", methods=["POST"])
# def login():

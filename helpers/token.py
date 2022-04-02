from flask import jsonify, request
from functools import wraps
from app import app
import jwt
import datetime


def generate_token(user_id, role):
    token = jwt.encode({
        "user_id": user_id,
        "role": role,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(days=90)},
        app.config["SECRET_KEY"], algorithm="HS256")
    return token


def get_user_data(headers):
    try:
        token = headers.get('Authorization').split()[1]
        return jwt.decode(token, app.config["SECRET_KEY"], algorithms=["HS256"])
    except:
        return None


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        try:
            if not (token := request.headers.get('Authorization')):
                return jsonify({"error": "Missing Token."})
            token = token.split()[1]

            data = jwt.decode(
                token, app.config["SECRET_KEY"], algorithms=["HS256"])
        except:
            return jsonify({
                "code": 1,
                "error": "Token is invalid"
            }), 401

        return f(*args, **kwargs)
    return decorated_function

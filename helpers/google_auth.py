import os
from google.oauth2 import id_token
from google.auth.transport import requests


def verify_token(token):
    try:
        # Specify the CLIENT_ID of the app that accesses the backend:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), os.environ.get("GOOGLE_CLIENT_ID"))

        if idinfo["email_verified"] == False:
            return None


        # ID token is valid. Get the user's Google Account ID from the decoded token.
        user_info = {
            "sub": idinfo["sub"],
            "email": idinfo["email"],
            "name": idinfo["name"], 
            "picture": idinfo["picture"], 
            "given_name": idinfo["given_name"], 
            "family_name": idinfo["family_name"]
        }

        return user_info
    except ValueError:
        # Invalid token
        return None

import re


def is_email(email):
    r = r'^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    return False if re.fullmatch(r, email) == None else True

def is_username(username):
    r = r'^[A-Za-z][A-Za-z0-9_]{7,29}$'
    return False if re.fullmatch(r, username) == None else True

def valid_password(password):
    r = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$'
    return False if re.fullmatch(r, password) == None else True


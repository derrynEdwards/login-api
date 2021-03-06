from flask import request
from datetime import datetime as dt
from flask import current_app as app
from .models import db, User
from .response import response

@app.route('/', methods=['GET'])
def keepalive():
    """
        Keepalive to ensure the app is running.
    """
    return str(dt.now())

@app.route('/api/createuser', methods=['POST'])
def create_user():
    """ 
        API Endpoint that will receive a POST request to create a user.
        Requires:
            username - String
            password - String
            email - String
    """
    username = request.json.get('username')
    password = request.json.get('password')
    email = request.json.get('email')

    if username is None or password is None or email is None:
        return (response(False, message="Incomplete or No parameters received."), 400)
    if (User.query.filter_by(username=username).first() is not None or
            User.query.filter_by(email=email).first() is not None):
        return (response(False, message="Username or email already exists."), 400)

    new_user = User(username=username,
                    password=password,
                    email=email,
                    created=dt.now(),
                    admin=False)
    db.session.add(new_user)
    db.session.commit()

    return (response(True, {"username": username}, "User created successfully."))

@app.route('/api/auth', methods=['POST'])
def auth_user():
    """
        API Endpoint that will receive a POST request to authenticate a user.
        Requires:
            username - String
            password - String
    """
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None:
        return (response(False, message="Incomplete or No parameters received."), 400)
    if User.query.filter_by(username=username, password=password).first() is not None:
        return (response(True, {"username": username, "logged_in": True}), 200)
    else:
        return (response(False, {"logged_in": False}, "Invalid username or password."), 400)
        
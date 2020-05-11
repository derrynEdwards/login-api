from flask import request, jsonify
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
        return (jsonify({'status': 'Failed', 'error': 'Incomplete or No parameters received.'}), 400)
    if (User.query.filter_by(username=username).first() is not None or
            User.query.filter_by(email=email).first() is not None):
        return (jsonify({'status': 'Failed', 'error': 'Username or email already exists.'}), 400)

    new_user = User(username=username,
                    password=password,
                    email=email,
                    created=dt.now(),
                    admin=False)
    db.session.add(new_user)
    db.session.commit()

    return (jsonify({'username': username, 'status': 'Success'}), 201)

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
        #return (jsonify({'status': 'Failed', 'data': None, 'error': 'Incomplete or No parameters received.'}), 400)
        return (response(False, None, "Incomplete or No parameters received."), 400)
    if User.query.filter_by(username=username, password=password).first() is not None:
        #return (jsonify({'status': 'Success', 'data': {'username': username, 'logged_in': True}, 'message': ''}), 200)
        return (response(True, {"username": username, "logged_in": True}, ""), 200)
    else:
        #return(jsonify({'status': 'Failed', 'data': {'logged_in': False}, 'error': 'Invalid username or password.'}), 400)
        return (response(False, {"logged_in": False}, "Invalid username or password."), 400)
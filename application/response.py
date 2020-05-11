from flask import jsonify

def response(status, data, message):
    '''
        Returns an error response in json format.
        Params:
            - status bool: True or False
            - data dict: Dictionary with data required as an api response
            - message str: Message to be returned as an api response
        Returns the API response in JSON format.
    '''

    if status:
        return jsonify({"status": True, "data": data, "message": message})
    else:
        return jsonify({"status": False, "data": data, "error": message})
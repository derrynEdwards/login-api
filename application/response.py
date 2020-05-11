from flask import jsonify

def response(status, data=None, message=None):
    '''
        Generates a response in json format.
        Params:
            - status bool: True or False
            - data dict: Dictionary with data required as an api response
            - message str: Message to be returned as an api response
        Returns the API response in JSON format.
    '''

    if status:
        return jsonify({"status": 'Success', "data": data, "message": message})
    else:
        return jsonify({"status": 'Failed', "data": data, "error": message})
        
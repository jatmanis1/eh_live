from flask_restful import Resource
from flask import make_response
from flask_jwt_extended import unset_access_cookies

class LogoutAPI(Resource):
    def get(self):
        response = make_response({"message": "You have been successfully logged out."})
        unset_access_cookies(response)  
        return response


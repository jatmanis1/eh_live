from flask_restful import Resource
from flask import request, jsonify
from ..models import User
from flask_jwt_extended import create_access_token, set_access_cookies
from datetime import timedelta

class LoginAPI(Resource):
    def post(self):
        # Get the JSON data sent in the request
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')

        # Query the database for the user
        user = User.query.filter_by(user_username=username).first()
        print(user)
        # Check if user exists and password is correct
        if not user or not user.check_pass(password):  
            return {'message': 'Invalid username or password'}, 200
            # response = jsonify({'message':'INvalid Username or password'})
            # return response

        # Create the JWT token with expiration time
        # access_token = create_access_token(identity=str(user.user_username), expires_delta=timedelta(hours=2))

        # # Create a response message
        # response = jsonify({'message': 'login success'})

        # # Set the access token as a cookie
        # set_access_cookies(response, access_token)

        # # Return the response with the access token and cookies set
        # return response 


        # data = request.get_json()
        #         username = data.get('username')
        #         password = data.get('password')

        #         user = User.query.filter_by(username=username).first()
        #         if not user or not user.password ==password:  
        #             return {'message': 'Invalid username or password'}, 401

        response = jsonify({'message':'login success'})
        access_token = create_access_token(identity=str(user.user_username), expires_delta=timedelta(hours=2))
        set_access_cookies(response, access_token)
        response = jsonify({'message':'login success', 'token': access_token,'user':user.to_dict()})
        return response

from flask_restful import Resource
from flask import request, jsonify
import requests
from werkzeug.security import generate_password_hash
from ..models import User, db  # Ensure correct import

class RegisterAPI(Resource):
    def get(self):
        """Test API for login"""
        payload = {"username": "mj", "password": "mj"}
        try:
            response = requests.post('http://127.0.0.1:5000/api/login', json=payload)
            return response.json(), response.status_code
        except requests.exceptions.RequestException as e:
            return {"error": str(e)}, 500

    def post(self):
        """Register a new user and auto-login"""
        data = request.get_json()
        if not data:
            return {"error": "No data provided"}, 400
        
        username = data.get('username')
        email = data.get('user_email')
        password = data.get('password')
        pincode = data.get('user_pincode')
        address = data.get('user_address')
        role = data.get('role', 'customer')

        if not username or not password or not email:
            return {"error": "Missing required fields"}, 400

        if User.query.filter_by(user_username=username).first():
            return {'message': 'Username already exists'}, 400

        # Hash the password before saving
        hashed_password = generate_password_hash(password)

        # Create new user
        new_user = User(
            user_name=username, 
            user_username=username, 
            user_password=password,  # Secure password
            user_address=address, 
            user_email=email, 
            user_pincode=pincode
        )

        try:
            db.session.add(new_user)
            db.session.commit()

            # Auto-login the user
            payload = {"username": new_user.user_username, "password": password}  # Use plain password for login
            response = requests.post('http://127.0.0.1:5000/api/login', json=payload)

            if response.status_code != 200:
                return {'message': 'User registered, but login failed', "error": response.json()}, 201

            return {'message': 'User registered successfully', "response": response.json()}, 201

        except Exception as e:
            db.session.rollback()
            return {"error": "Database error", "details": str(e)}, 500

    def put(self, id):
        """Update user profile (convert to pro)"""
        data = request.get_json()
        if not data:
            return {"error": "No data provided"}, 400

        user = User.query.filter_by(id=id).first()
        if not user:
            return {"error": "User not found"}, 404

        try:
            user.user_service = data.get('user_service', user.user_service)
            user.user_role = 'pro'
            user.user_exp = data.get('user_exp', user.user_exp)

            db.session.commit()
            return {"msg": "Pro profile updated successfully"}, 200

        except Exception as e:
            db.session.rollback()
            return {"error": "Database error", "details": str(e)}, 500

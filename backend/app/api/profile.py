from flask_restful import Resource
from flask import request, jsonify
from ..models import db, User
from flask_jwt_extended import get_jwt_identity, jwt_required

class ProfileApi(Resource):
    @jwt_required()
    def get(self):
        user_username = get_jwt_identity()
        print(user_username,'fghjkl')
        user = User.query.filter_by(user_username=user_username).first()

        if not user:
            return {"message": "Uwwser not found"}, 200

        return jsonify({
            "user_name": user.user_name,
            "user_username": user.user_username,
            "user_email": user.user_email,
            "user_address": user.user_address,
            "user_pincode": user.user_pincode,
            "user_role": user.user_role,
            "user_exp": user.user_exp,
            "user_desc": user.user_desc,
            "user_rating": user.user_rating,
            "user_status": user.user_status
        })

    @jwt_required()
    def put(self):
        user_username = get_jwt_identity()
        user = User.query.filter_by(user_username=user_username).first()

        if not user:
            return {"message": "User notgg found"}, 404

        data = request.json

        # user.user_username = 'admin'
        user.user_name = data.get("user_name", user.user_name)
        user.user_email = data.get("user_email", user.user_email)
        user.user_address = data.get("user_address", user.user_address)
        user.user_pincode = data.get("user_pincode", user.user_pincode)
        user.user_exp = data.get("user_exp", user.user_exp)
        user.user_desc = data.get("user_desc", user.user_desc)

        db.session.commit()
        return {"message": "Profile updated successfully"}

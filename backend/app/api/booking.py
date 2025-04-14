from flask_restful import Resource
from flask import request, jsonify
from ..models import User, db, ServiceRequest, Services
from flask_jwt_extended import get_jwt_identity, jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc, func
from datetime import datetime

class BookingApi(Resource):

    @jwt_required()
    def put(self):
        return {"msg": "Request Created"}

    @jwt_required()
    def get(self, id):
        requests = ServiceRequest.query.filter_by(req_pro_id=id).all()
        user = User.query.filter_by(id=id).first()

        if not user:
            return {"msg": "User not found"}, 404

        service = Services.query.filter_by(id=user.user_service).first()
        requests_list = [request.to_dict() for request in requests]

        return {
            "recent_services": requests_list,
            "user": user.to_dict() if user else None,
            "service": service.to_dict() if service else None,
            "success": True
        }

    @jwt_required()
    def post(self, id):
        current_user_username = get_jwt_identity()
        current_user = User.query.filter_by(user_username=current_user_username).first()

        if not current_user:
            return {"msg": "Unauthorized user"}, 401

        pro = User.query.filter_by(id=id).first()
        if not pro:
            return {"msg": "Invalid professional ID"}, 200

        if pro.user_role != 'pro':
            return {"msg": "Selected user is not a pro"}, 200

        if pro.is_verified and pro.user_status == 'blocked':
            return {"msg": "Selected user is not not verified or blocked"}, 200

        service1 = Services.query.filter_by(id=1).first()
        if not service1:
            return {"msg": "Service Not Found"}, 404

        # Creating a new booking
        new_booking = ServiceRequest(
            req_cust_id=current_user.id,
            req_pro_id=pro.id,
            req_service_id=service1.id
        )
        db.session.add(new_booking)
        db.session.commit()

        return {"msg": "New Service Request Created", "success": True}, 201

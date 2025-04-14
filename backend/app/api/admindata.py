
from flask_restful import Resource
from flask import request,jsonify
from ..models import User, db,ServiceRequest,Services
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc, func
from datetime import datetime

class AdminDataApi(Resource):
    @jwt_required()
    def get(self):


        # Query status counts for professionals
        pro_status = db.session.query(User.user_status, func.count(User.user_status))\
            .filter(User.user_role == 'pro')\
            .group_by(User.user_status)\
            .all()

        # Query status counts for customers
        cust_status = db.session.query(User.user_status, func.count(User.user_status))\
            .filter(User.user_role == 'cust')\
            .group_by(User.user_status)\
            .all()

        # Query status counts for service requests
        req_status = db.session.query(ServiceRequest.req_status, func.count(ServiceRequest.req_status))\
            .group_by(ServiceRequest.req_status)\
            .all()

        # Convert results into dictionary format
        data = {
            "pro_status": {status: count for status, count in pro_status},
            "cust_status": {status: count for status, count in cust_status},
            "req_status": {status: count for status, count in req_status}
        }

        return jsonify(data)

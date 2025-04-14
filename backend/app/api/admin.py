

from flask_restful import Resource
from flask import request,jsonify
from ..models import User, db,ServiceRequest,Services
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc, func
from datetime import datetime

# class AdminProApi(Resource):
    # @jwt_required()
    # def get(self):
    #     current_user_username = get_jwt_identity()
    #     current_user = User.query.filter_by(user_username = current_user_username).first()
    #     date_str= datetime.now().strftime('%Y-%m-%d')
    #     date_date = datetime.strptime(date_str, '%Y-%m-%d')
    #     pros = User.query.filter(User.user_date == "2024-09-26").all()
        
    #     pro_status =  db.session.query(User.user_status, func.count(User.user_status)).group_by(User.user_status).filter(User.user_role =='pro').all()
    #     cust_status =  db.session.query(User.user_status, func.count(User.user_status)).filter(User.user_role =='cust').group_by(User.user_status).all()
    #     req_status =  db.session.query(ServiceRequest.req_status, func.count(ServiceRequest.req_status)).group_by(ServiceRequest.req_status).all()

    #     return {"msg":"no data for now, only graph "}



    
from flask_restful import Resource
from flask import request,jsonify
from ..models import User, db,ServiceRequest,Services
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc, func
from datetime import datetime

class AdminDataApi(Resource):
    # @jwt_required()
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

        # Convert to separate key-value lists
        def format_status(status_data):
            return {
                "keys": [status for status, count in status_data if status],
                "values": [count for status, count in status_data if status]
            }

        data = {
            "pro_status": format_status(pro_status),
            "cust_status": format_status(cust_status),
            "req_status": format_status(req_status)
        }
        print(data)

        return jsonify(data)


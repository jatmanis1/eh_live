from flask_restful import Resource
from flask import request, jsonify
from ..models import User,Services, ServiceRequest

class ServiceApi(Resource):
    def get(self, id):
        service = Services.query.filter_by(id=id).first()
        print(service)
        pros = User.query.filter_by(user_service = id).all()
        req_h = ServiceRequest.query.filter_by()
        pros =[pro.to_dict() for pro in pros]
        if service : service = service.to_dict()
        # for i in pros :
        #     print(i.to_dict())
        return {"service": service,"pros":pros}
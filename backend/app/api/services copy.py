from flask_restful import Resource
from flask import request, jsonify
from ..models import User,Services

class ServicesApi(Resource):
    def get(self):
        services = Services.query.all()
        return {"services": services}
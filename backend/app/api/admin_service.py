

from flask_restful import Resource
from flask import request, jsonify
from ..models import User, db, ServiceRequest,Services
from flask_jwt_extended import get_jwt_identity, jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc
from ..models import ServiceRequest
# from flask_wtf.csrf import CSRFProtect, csrf_exempt
# csrf = CSRFProtect()


class AdminServiceApi(Resource):
    # @jwt_required()
    def get(self,id=None):
        serv = Services.query.all()
        services = [service.to_dict() for service in serv],
        print(services[0])
        return jsonify({"services":services[0]})
    @jwt_required()
    def post(self,id=None):
        data = request.get_json()
        serv=data.get('flag')
        # print(serv,"fghgfghhf")
        flag2 = False
        serv_name = str(data.get('service_name'))
        flag1= False
        service1=Services.query.filter(Services.service_name == "service2").first()
        print(service1, data)
        flag2 = True
        if request.method=='POST' and not service1:
            service_type= data.get('service_name')
            desc= data.get('service_desc')
            base_p= data.get('service_b_price')
            time_required= data.get('time_required')
            new_service = Services( service_name= service_type,service_desc=desc, service_b_price=base_p, time_required=time_required)
            db.session.add(new_service)
            db.session.commit()
            return jsonify({ "msg": "Service Added Successfully"})
        else : return jsonify({"msg": "service name already exist"})
            # return redirect('/admin_service')
    
    @jwt_required()
    def put(self, id):
        data = request.get_json()

        if data:
            service1=Services.query.filter_by(id =id).first()
            flag1=True

            print(service1,'sdvfds', data)
            if request.method=='PUT' and service1:
                service1.service_name= data.get('service_name')
                service1.service_desc= data.get('service_desc')
                service1.service_b_price= data.get('service_b_price')
                service1.time_required= data.get('time_required')
                db.session.commit()
                
                return jsonify({ "msg": "Service updated Successfully"})
            
            return jsonify({ "msg": "Service Not found"})
                # return redirect("/admin_service")
        # return render_template("admin_service_add.html", flag1=flag1,flag2=flag2, services=service1)


    @jwt_required()
    def delete(self, id):

        service1=Services.query.filter_by(id =id).first()
        flag1=True
        print(service1,'sdvfds')
        if request.method=='DELETE' and service1:
            db.session.delete(service1)
            db.session.commit()
            return jsonify({ "msg": "Service deleted Successfully"})
            
        return jsonify({ "msg": "Service Not found"})
                # return redirect("/admin_service")
        # return render_template("admin_service_add.html", flag1=flag1,flag2=flag2, services=service1)



from flask_restful import Resource
from flask import request, jsonify
from ..models import User, db
from flask_jwt_extended import get_jwt_identity, jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc
from ..models import ServiceRequest
# from flask_wtf.csrf import CSRFProtect, csrf_exempt
# csrf = CSRFProtect()


class AdminProApi(Resource):
    @jwt_required()
    def get(self, id=None):
        # current_user_username = get_jwt_identity()
        # current_user = User.query.filter_by(user_username=current_user_username).first()

        try:
            # if not current_user.user_role :#!= 'admin':
            #     return {'message': 'User is not authorized to access this resource'}, 403

            page = request.args.get('page', 1, int)
            per_page = 5
            pros = User.query.filter_by(user_role='pro').order_by(desc(User.user_rating)).paginate(page=page, per_page=per_page)
            pros = [pro.to_dict() for pro in pros.items]


            return {
                "no. of user":len(pros),
                "pros": pros

            }, 200

        except DecodeError:
            return {'message': 'Invalid token format. Please provide a valid JWT.'}, 400
        except Exception as e:
            # app.logger.error(f"Error in AdminProApi: {e}")
            return {'message': 'An unexpected error occurred'}, 500

    @jwt_required()
    def put(self, id):
        user = User.query.filter_by(id=id).first()
        data = request.get_json()
        status = data.get('status')
        is_verified = data.get('is_verified',9)
        response ={}
        if not user:
            return {'message': 'user not found'}, 404
        if request.method =='PUT': 
            if status: 
                user.user_status= status
                response['status updated to']=status

            if is_verified ==0 or is_verified==1: 
                user.is_verified =is_verified
                response['is_verified_updated to']= is_verified
                print('verifed')
            db.session.commit()
            # if status =='block':
            #     print(11)
            #     req_serv = ServiceRequest.query.filter(ServiceRequest.req_pro_id == id).all()
            #     for service in req_serv:
            #         if service.req_status == 'Accepted':
            #             service.req_status = 'Rejected'
                        # print(21)
            
           
        return response, 200



    
# @app.route("/pro/<pro_id>", methods = ['POST','GET'])
# def admin_pro_edit(pro_id):
#     pro_id1 = pro_id
#     user =User.query.filter_by(id = pro_id1).first()
#     # print(pro1.user_status)
    
#     status = ['block', 'allow']
    
#     if request.method =='POST': 
#         status =str(request.form.get('user_status'))
#         is_verified =str(request.form.get('verify'))
#         if status1 =='block':
#             req_serv = ServiceRequest.query.filter(ServiceRequest.req_pro_id == pro_id1).all()
#             for service in req_serv:
#                 if service.req_status == 'Accepted':
#                     service.req_status = 'Rejected'
#         if status1: pro1.user_status= status1
#         if verify1 : 
#             pro1.is_verified =True
#             print('verifed')
#         db.session.commit()
           
#     return render_template('admin_pro_edit.html',status= status, pro=pro1)

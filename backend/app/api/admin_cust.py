

from flask_restful import Resource
from flask import request,jsonify
from ..models import User, db
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import jwt_required
from jwt.exceptions import DecodeError
from sqlalchemy import desc


class AdminCustApi(Resource):
    @jwt_required()
    def get(self, id=None):
        current_user_username = get_jwt_identity()
        current_user = User.query.filter_by(user_username = current_user_username).first()
        
        try:
            if  current_user.user_role :#=='pro':
                page = request.args.get('page',1,int)
                per_page = 5
                custs= User.query.order_by(desc(User.user_rating)).all()#.paginate(page=page, per_page=per_page)
                print(custs,'mjj')
                custs = [cust.to_dict() for cust in custs]
                return jsonify({
                    "no. of user found":len(custs),
                    "custs":custs
                })
            else:return jsonify({"message": "User is not admin"}), 401

        except DecodeError as e:
            return {'message': 'Invalid token format. Please provide a valid JWT.'}, 400
        except Exception as e:
            # General error handling
            print(e)
            return {'message': str(e)}, 500



    @jwt_required()
    def put(self, id):
        print(id,"id")
        user = User.query.filter_by(id=id).first()
        if not user:
            return {"msg":'User not found'},200
        data = request.get_json()
        # print(data.get('id'),'adfsgnv')
        status = data.get('status')
        verify = (data.get('verify'))
        if verify  =='1' or verify =="0":
            verify = int(verify)
                  
        response = {}
        if status :
            user.user_status = status
            response['user_status']=status
        if verify==1 :
            user.is_verified = int(verify)
            response['is_verified']=int(verify)
        elif verify ==0:
            db.session.delete(user)

        db.session.commit()

        return response

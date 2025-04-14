from flask_restful import Resource
from flask import request,jsonify
from ..models import User, db, ServiceRequest, Services
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_jwt_extended import verify_jwt_in_request, jwt_required
from jwt.exceptions import DecodeError
from datetime import datetime,date
from sqlalchemy import desc, and_ , or_, func


class DashboardAPI(Resource):
    @jwt_required()
    def post(self):
        # return jsonify({"msg": "fdsdfgfedf"}),200
        return 'mj'


    @jwt_required()
    def get(self, id=None):
        current_user = get_jwt_identity()
        # token = request.headers.get('Authorization', '').split('Bearer ')[-1]
        # print(f"Received token: {token}")  # Log token to see its contents
        print(current_user,'cruser')
        # return {'message': 'access granted to user dashboard', "user":current_user}, 201
        try:
            # Your token-related logic
            user_username = get_jwt_identity()
            
            current_user = User.query.filter_by(user_username = user_username).first()
            # return {'message': 'access granted to user dashboard', "user":current_user}, 201
        

        
            accept_count = -1
            service1 = False
            user = current_user
            user_serv = False
            request_created = False
            typek = False
            service_pending = None
            service_history = None
            page_p = request.args.get('page_p', 1, int)
            page_h = request.args.get('page_h', 1, int)
            per_page = 5
            accept_count_allowed = 0

            if current_user:
                # # Customer logic
                # print(current_user)
                if current_user.user_role == 'cust':
                    request_created = ServiceRequest.query.filter_by(req_cust_id=user.id).all()
                #     # request_created = ServiceRequest.query.filter_by(req_cust=user).all()
                # #     accept_count = request_created
                    service_pending = ServiceRequest.query.filter(
                        and_(
                            ServiceRequest.req_cust_id == user.id,
                            or_(
                                ServiceRequest.req_status == 'Accepted',
                                ServiceRequest.req_status == 'Pending'
                            )
                        )
                    ).paginate(page=page_h, per_page=per_page)

                    service_history = ServiceRequest.query.filter(
                        and_(
                            ServiceRequest.req_cust_id == user.id,
                            or_(
                                ServiceRequest.req_status == 'Rejected',
                                ServiceRequest.req_status == 'Closed'
                            )
                        )
                    ).paginate(page=page_h, per_page=per_page)

                #     accept_count = db.session.query(ServiceRequest.req_status, func.count(ServiceRequest.req_status)).filter(
                #         ServiceRequest.req_cust_id == user.id).group_by(ServiceRequest.req_status).all()

                # Professional logic
                # elif current_user.user_role == 'pro':
                #     user = current_user
                #     user_serv = Services.query.filter_by(id=user.user_service).first()
                #     service1 = Services.query.filter_by(id=user.user_service).first()
                #     request_created = ServiceRequest.query.filter_by(req_pro_id=user.id).all()

                #     servi = ServiceRequest.query.filter_by(req_pro_id=user.id).all()

                    # service_pending = ServiceRequest.query.filter(
                    #     and_(
                    #         ServiceRequest.req_pro_id == user.id,
                    #         or_(
                    #             ServiceRequest.req_status == 'Accepted',
                    #             ServiceRequest.req_status == 'Pending'
                    #         )
                    #     )
                    # ).paginate(page=page_h, per_page=per_page)

                    # service_history = ServiceRequest.query.filter(
                    #     and_(
                    #         ServiceRequest.req_pro_id == user.id,
                    #         or_(
                    #             ServiceRequest.req_status == 'Rejected',
                    #             ServiceRequest.req_status == 'Closed'
                    #         )
                    #     )
                    # ).paginate(page=page_h, per_page=per_page)

                    # accept_count = db.session.query(ServiceRequest.req_status, func.count(ServiceRequest.req_status)).filter(
                    #     ServiceRequest.req_pro_id == user.id).group_by(ServiceRequest.req_status).all()

                #     for i in accept_count:
                #         if i[0] == 'Accepted':
                #             accept_count_allowed = i[1]

                # Handle POST request actions: accept, reject, close
                
                    return jsonify({
                        "user_serv": user_serv,
                        "page_p": page_p,
                        "page_h": page_h,
                        "service1": service1,
                        "service_history": [service.to_dict() for service in service_history.items],  # Assuming ServiceRequest has `to_dict()` method
                        "service_pending": [service.to_dict() for service in service_pending.items],
                        "request_created": [req.to_dict() for req in request_created],
                        # "user": user.to_dict(),  # Assuming the User model has a `to_dict()` method
                        "accept_count": accept_count,
                        "accept_count_allowed": accept_count_allowed
                    })
                elif current_user.user_role == 'pro':
                    request_created = ServiceRequest.query.filter_by(req_pro_id=user.id).all()
                #     # request_created = ServiceRequest.query.filter_by(req_cust=user).all()
                # #     accept_count = request_created
                    service_pending = ServiceRequest.query.filter(
                        and_(
                            ServiceRequest.req_pro_id== user.id,
                            or_(
                                ServiceRequest.req_status == 'Accepted',
                                ServiceRequest.req_status == 'Pending'
                            )
                        )
                    ).paginate(page=page_h, per_page=per_page)

                    service_history = ServiceRequest.query.filter(
                        and_(
                            ServiceRequest.req_pro_id == user.id,
                            or_(
                                ServiceRequest.req_status == 'Rejected',
                                ServiceRequest.req_status == 'Closed'
                            )
                        )
                    ).paginate(page=page_h, per_page=per_page)

                #     accept_count = db.session.query(ServiceRequest.req_status, func.count(ServiceRequest.req_status)).filter(
                #         ServiceRequest.req_cust_id == user.id).group_by(ServiceRequest.req_status).all()

                # Professional logic
                # elif current_user.user_role == 'pro':
                #     user = current_user
                #     user_serv = Services.query.filter_by(id=user.user_service).first()
                #     service1 = Services.query.filter_by(id=user.user_service).first()
                #     request_created = ServiceRequest.query.filter_by(req_pro_id=user.id).all()

                #     servi = ServiceRequest.query.filter_by(req_pro_id=user.id).all()

                    # service_pending = ServiceRequest.query.filter(
                    #     and_(
                    #         ServiceRequest.req_pro_id == user.id,
                    #         or_(
                    #             ServiceRequest.req_status == 'Accepted',
                    #             ServiceRequest.req_status == 'Pending'
                    #         )
                    #     )
                    # ).paginate(page=page_h, per_page=per_page)

                    # service_history = ServiceRequest.query.filter(
                    #     and_(
                    #         ServiceRequest.req_pro_id == user.id,
                    #         or_(
                    #             ServiceRequest.req_status == 'Rejected',
                    #             ServiceRequest.req_status == 'Closed'
                    #         )
                    #     )
                    # ).paginate(page=page_h, per_page=per_page)

                    # accept_count = db.session.query(ServiceRequest.req_status, func.count(ServiceRequest.req_status)).filter(
                    #     ServiceRequest.req_pro_id == user.id).group_by(ServiceRequest.req_status).all()

                #     for i in accept_count:
                #         if i[0] == 'Accepted':
                #             accept_count_allowed = i[1]

                # Handle POST request actions: accept, reject, close
                
                    return jsonify({
                        "user_serv": user_serv,
                        "page_p": page_p,
                        "page_h": page_h,
                        "service1": service1,
                        "service_history": [service.to_dict() for service in service_history.items],  # Assuming ServiceRequest has `to_dict()` method
                        "service_pending": [service.to_dict() for service in service_pending.items],
                        "request_created": [req.to_dict() for req in request_created],
                        # "user": user.to_dict(),  # Assuming the User model has a `to_dict()` method
                        "accept_count": accept_count,
                        "accept_count_allowed": accept_count_allowed
                    })
                else:
                    return {"message": "your role is not pro/cust"}
            else:
                return jsonify({"message": "User not authenticated"}), 401
        
        except DecodeError as e:
            # Handle the case where the token is invalid
            return {'message': 'Invalid token format. Please provide a valid JWT.'}, 400
        except Exception as e:
            # General error handling
            return {'message': str(e)}, 500
    

    @jwt_required()
    def put(self, id ):
        current_user = get_jwt_identity()
        data = request.get_json()
        print(current_user,'cruser')
        remarks = data.get('req_remarks')
        rating = data.get('req_rating')
        # print(rating, remarks, data['req_rating'])
        try:
            user_username = get_jwt_identity()            
            current_user = User.query.filter_by(user_username = user_username).first()
            req  = ServiceRequest.query.filter_by(id=id).first()
            print(req)
            
            if rating:req.req_rating=rating
            if remarks:req.req_remark=remarks
            db.session.commit()
            if data['update'] == 'accept':
            
                req.update_status("Accepted")
                db.session.commit()
            elif data['update'] == 'close':
                print(data.get('remarks'))
                print(data.get('rating'))
                req.update_status("Closed")
                # req.req_rating=rating
                # req.req_remark=remarks
                db.session.commit()   
                print(req.req_rating)
            elif data['update'] == 'reject':
                req.update_status("Rejected")
                db.session.commit()
            
        except DecodeError as e:
            return {'message': 'Invalid token format. Please provide a valid JWT.'}, 400
        except Exception as e:
            print(e)
            return {'message': str(e)}, 500

# if request.method == 'POST':
#                     accept = request.form.get('accept')
#                     reject = request.form.get('reject')
#                     close = request.form.get('close')
#                     rating = request.form.get("rating")
#                     remark = request.form.get("remark")

#                     if accept:
#                         # Call the function to accept the request
#                         req_accept(accept)

#                     elif reject:
#                         req_reject(reject)

#                     elif close:
#                         req_close(close)
#                         return jsonify({"message": f"Request {close} closed successfully"})





# @app.route("/accept/<req_id>")
def req_accept(req_id):
    r_id = req_id
    req = ServiceRequest.query.filter(ServiceRequest.id == r_id).first()
    if req:
        req.req_status = "Accepted"
        req.set_action_date = datetime.now().strftime('%Y-%m-%d')
        db.session.commit()

# @app.route("/reject/<req_id>")
def req_reject(req_id):
    r_id = req_id
    req = ServiceRequest.query.filter(ServiceRequest.id == r_id).first()
    # print(req)
    if req:
        req.req_status = "Rejected"
        req.set_action_date = datetime.now().strftime('%Y-%m-%d')
        req.set_completed_date  =  datetime.now().strftime('%Y-%m-%d')
        db.session.commit()

# @app.route("/close/<req_id>")
def req_close(req_id):

    r_id = req_id
    req = ServiceRequest.query.filter(ServiceRequest.id == r_id).first()
    if req:
        req.req_status = "Closed"
        req.req_completed_date  =  date.today()
        db.session.commit()

# @app.route("/remarks/<req_id>", methods =['POST', 'GET'])
# @login_required
# @cust_only
# def remarks(req_id):
#     r_id = req_id
#     req = ServiceRequest.query.filter(ServiceRequest.id == r_id).first()
#     pr_id = req.req_pro_id
#     pro_d =User.query.filter_by(id = pr_id).first()
#     if request.method == 'POST':
#         rating = request.form.get("rating")
#         remark = request.form.get("remark")
#         if req:
#             req.req_rating = rating
#             req.req_remark = remark 
#             db.session.commit()
#             pro_d.pro_rating = user_rating(pr_id)
#             db.session.commit()
#             return redirect("/dashboard")

#     return render_template("rating.html")
# @app.route("/avg/<pro_id>")
def user_rating(pro_id):
    pr1= pro_id
    all1 = ServiceRequest.query.filter(ServiceRequest.req_pro_id == pr1).all()
    # print(all1)
    count, total , flag= 0, 0, False
    for i in all1 :
        if i.req_rating:
            count +=1
            total += i.req_rating 
            flag = True
            # print(i.req_rating, total, count)
    if flag : return f"{total/count:.2f}"
    return 0 

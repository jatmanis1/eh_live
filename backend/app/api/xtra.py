
# @app.route("/pro")
# def admin_pro():
#     page = request.args.get('page',1,int)
#     per_page = 5
#     pros= User.query.filter_by(user_role ='pro').order_by(desc(User.user_rating)).paginate(page=page, per_page=per_page)
#     return render_template('admin_pro.html', pros= pros)

# @app.route("/pro/<pro_id>", methods = ['POST','GET'])
# def admin_pro_edit(pro_id):
#     pro_id1 = pro_id
#     pro1 =User.query.filter_by(id = pro_id1).first()
#     # print(pro1.user_status)
    
#     status = ['block', 'allow']
    
#     if request.method =='POST': 
#         status1 =str(request.form.get('user_status'))
#         verify1 =str(request.form.get('verify'))
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

# @app.route("/cust")
# @login_required
# @admin_only
# def admin_cust():
#     page = request.args.get('page',1,int)
#     per_page = 5
#     custs= User.query.filter_by(user_role ='cust').order_by(desc(User.user_rating)).paginate(page=page, per_page=per_page)
#     return render_template('admin_cust.html', custs= custs)


# @app.route("/cust/<cust_id>", methods = ['POST','GET'])
# @login_required
# def admin_cust_edit(cust_id):
#     cust_id1 = cust_id
#     cust1 =User.query.filter_by(id = cust_id1).first()

#     status = ['block', 'allow']
    
#     if request.method =='POST': 
#         status1 =str(request.form.get('cust_status'))
#         verify1 =str(request.form.get('verify'))
#         print(verify1, status1)
#         if status1 =='ban':
#             req_serv = ServiceRequest.query.filter(ServiceRequest.req_cust_id == cust_id1).all()
#             for service in req_serv:
#                 if service.req_status == 'Accepted':
#                     service.req_status = 'Rejected'
#         if status1: cust1.user_status= status1
#         if verify1 : 
#             cust1.is_verified =True
#             print('verifed cust')
#         db.session.commit()
           
#     return render_template('admin_cust_edit.html',status= status, cust= cust1)


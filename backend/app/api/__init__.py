from flask import request, jsonify
from flask_restful import Resource, Api
from flask_jwt_extended import jwt_required, get_jwt_identity
from app.models import db, User

# Initialize Flask-RESTful API
api = Api()

class UserProfileAPI(Resource):
    @jwt_required()
    def get(self):
        user_id = get_jwt_identity()
        user = User.query.get(user_id)

        if not user:
            return {'message': 'User not found'}, 404

        return {
            'id': user.id,
            'username': user.user_username,
            'email': user.user_email,
            'role': user.user_role
        }, 200

def initialize_routes(app):
    """Function to register API routes in Flask app"""

    # Import routes inside function to avoid circular import issues
    from app.api import login, register, logout, dashboard, admin, admin_cust, admin_pro, admin_service\
        , booking, service, profile
    # from app.api import trriger_job  # Corrected import

    api.add_resource(register.RegisterAPI, '/api/register', '/api/register/<id>')
    api.add_resource(login.LoginAPI, '/api/login')
    # api.add_resource(UserProfileAPI, '/api/profile')
    api.add_resource(logout.LogoutAPI, '/api/logout')
    api.add_resource(dashboard.DashboardAPI, '/api/user', '/api/user/<id>')
    api.add_resource(admin_pro.AdminProApi, '/api/admin/pro', '/api/admin/pro/<id>')
    api.add_resource(admin_cust.AdminCustApi, '/api/admin/cust', '/api/admin/cust/<id>')
    api.add_resource(admin_service.AdminServiceApi, '/api/admin/service', '/api/admin/service/<id>')
    api.add_resource(service.ServiceApi, '/api/service/<id>')
    api.add_resource(booking.BookingApi, '/api/booking', '/api/booking/<id>')
    api.add_resource(admin.AdminDataApi, '/api/admindata', '/api/admindata/<id>')
    api.add_resource(profile.ProfileApi, '/api/profile')
    # api.add_resource(trriger_job.JobApi, '/api/job', '/api/job/<id>')

    api.init_app(app)

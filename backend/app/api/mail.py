# # from task import send_async_email
# # from run import app
# from flask_restful import Resource
# from flask import request, jsonify
# # import requests
# from werkzeug.security import generate_password_hash
# from ..models import User, db  # Ensure correct import
# from .task import send_async_email

# # from app.task import
# # @app.route('/send-now/<email>')
# class MailApi(Resource):
#     def get(self,email):
#         """Send email immediately using Celery"""
#         task = send_async_email.apply_async(args=[email, "Test Email", "This is an immediate email."])
#         return f"📩 Email to {email} is being sent! Task ID: {task.id}"


#     # @app.route('/send-later/<email>')
#     def post(self,email):
#         """Send email after 1 minute using Celery"""
#         task = send_async_email.apply_async(args=[email, "Delayed Email", "This email was sent 1 minute later."], countdown=60)
#         return f"📩 Email to {email} will be sent in 1 minute! Task ID: {task.id}"



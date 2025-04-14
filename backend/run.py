from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies
from flask_cors import CORS
from datetime import timedelta
from flask_migrate import Migrate
import logging
from flask_mail import Mail, Message
from celery import Celery
# from run import app
# from flask import current_app
# Initialize Flask App
# app = Flask(__name__)
# from app import api
app = Flask(__name__)
# db = SQLAlchemy()

# Setup the Flask app configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'  # Change this to a secure secret
from app.models import db
# Initialize extensions
# db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)
db.init_app(app)
migrate = Migrate(app, db)  # Bind Migrate with Flask app and db

migrate.init_app(app, db)
jwt.init_app(app)
from app.models import User
from app.api import initialize_routes
initialize_routes(app)
# from flask_mail import Mail
mail = Mail
# Create the database
with app.app_context():
    db.create_all()

app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Outlook SMTP server
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'easyequity01@gmail.com'  # Your Outlook email
app.config['MAIL_PASSWORD'] = 'wcmdmwlnuhdbnryp'  # 🔥 Use an App Password
# app.config['MAIL_DEFAULT_SENDER'] = ('EasyEquity', 'easyequity01@outlook.com')
# app.config['MAIL_DEFAULT_SENDER'] = 'easyequity01@outlook.com'
app.config['MAIL_DEFAULT_SENDER'] = 'easyequity01@gmail.com'

# ✅ Celery Configuration (Redis as Broker & Backend)
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6369/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6369/0'
import socket
app.config['MAIL_HELO_HOSTNAME'] = socket.gethostname()

# ✅ Initialize Flask-Mail & Celery
mail = Mail(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# ✅ Configure Logging
logging.basicConfig(level=logging.INFO)


@celery.task(name="app.send_async_email")
def send_async_email(to_email, subject, body):
    """Send an email asynchronously using Flask-Mail"""
    try:
        with app.app_context():  # Ensures Flask context is available inside Celery
            msg = Message(subject, recipients=[to_email], body=body)
            mail.send(msg)
            logging.info(f"✅ Email sent successfully to {to_email}!")
            return f"✅ Email sent successfully to {to_email}!"
    except Exception as e:
        logging.error(f"❌ Email failed: {str(e)}")
        return f"❌ Email failed: {str(e)}"


@celery.task(name="app.send_async_email_doc")
def send_async_email_doc(to_email, subject, body, pdf_attachment ):
    """Send an email asynchronously using Flask-Mail"""
    try:
        with app.app_context():  # Ensures Flask context is available inside Celery
            msg = Message(subject, recipients=[to_email], body=body)
            msg.attach("monthly_report.pdf", "application/pdf", pdf_attachment)
            mail.send(msg)
            logging.info(f"✅ Email sent successfully to {to_email}!")
            return f"✅ Email sent successfully to {to_email}!"
    except Exception as e:
        logging.error(f"❌ Email failed: {str(e)}")
        return f"❌ Email failed: {str(e)}"


@celery.task(name="app.send_async_email_csv")
def send_async_email_csv(to_email, subject, body, csv_attachment ):
    """Send an email asynchronously using Flask-Mail"""
    try:
        with app.app_context():  # Ensures Flask context is available inside Celery
            msg = Message(subject, recipients=[to_email], body=body)
            msg.attach("completed_service_request.csv", "text/csv", csv_attachment)
            mail.send(msg)
            logging.info(f"✅ Email sent successfully to {to_email}!")
            return f"✅ Email sent successfully to {to_email}!"
    except Exception as e:
        logging.error(f"❌ Email failed: {str(e)}")
        return f"❌ Email failed: {str(e)}"


from flask_restful import Resource
from flask import request, jsonify
import csv
import io
from flask import render_template

# class JobApi(Resource):
#     def get(self):
#         """API endpoint to trigger CSV export job."""
        
#         task = export_completed_request.delay()  # Asynchronously run the Celery task
        
#         return jsonify({
#             "message": "CSV export job has been triggered successfully!",
#             "task_id": task.id
#         }), 202


@app.route("/hardcoded-route", methods=["GET"])
def hardcoded_function():
    return {"message": "This is a hardcoded route"}, 200


# @celery.task
@app.route('/job1')
def export_completed_request():
    """Exports completed service requests as a CSV and emails it to all admins."""
    
    from app.models import ServiceRequest, User  # Import inside function to avoid circular dependency
    # from run import send_async_email_csv
    
    # Fetch completed service requests
    completed_requests = ServiceRequest.query.filter_by(req_status='Closed').all()
    
    # CSV file setup
    output_buffer = io.StringIO()
    fieldnames = [
        'service_request_id', 'service_id', 'customer_id', 'service_professional_id',
        'request_date', 'completion_date', 'status', 'remarks', 'address', 'pincode'
    ]
    
    csv_writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
    csv_writer.writeheader()
    
    for request in completed_requests:
        csv_writer.writerow({
            'service_request_id': request.id,
            'service_id': request.req_service_id,
            'customer_id': request.req_cust_id,
            'service_professional_id': request.req_pro_id,
            'request_date': request.req_action_date.strftime('%Y-%m-%d %H:%M:%S'),
            'completion_date': request.req_completed_date.strftime('%Y-%m-%d %H:%M:%S') if request.req_completed_date else 'N/A',
            'status': request.req_status,
            'remarks': request.req_remark or 'N/A',
            'address': request.req_cust.user_address,
            'pincode': request.req_cust.user_pincode,
        })
    
    # Retrieve CSV content
    csv_data = output_buffer.getvalue()
    output_buffer.close()
    
    # Email content setup
    email_subject = 'EasyHome: Completed Service Requests Export'
    email_body = render_template('csv_export.html')
    
    # Fetch all admin users
    admin_users = User.query.filter_by(user_role='admin').all()
    print(admin_users)
    for admin in admin_users:
        send_async_email_csv(admin.user_email, email_subject, email_body, csv_data)
    return 'requested data will sent soon to your registered email'


# from app.tasks.celery import celery
# celery = init_celery(app)
# celery.conf.update(app.config)

if __name__ == '__main__':
    app.run(debug=True)

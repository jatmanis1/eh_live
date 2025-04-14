from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, set_access_cookies
from flask_cors import CORS
from datetime import timedelta
from flask_migrate import Migrate
import logging
from flask_mail import Mail, Message
from celery import Celery
import socket
import csv
import io

# ✅ Initialize Flask App
app = Flask(__name__)

# ✅ Setup Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'easyequity01@gmail.com'
app.config['MAIL_PASSWORD'] = 'wcmdmwlnuhdbnryp'
app.config['MAIL_DEFAULT_SENDER'] = 'easyequity01@gmail.com'
app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
app.config['MAIL_HELO_HOSTNAME'] = socket.gethostname()

# ✅ Initialize Extensions
db = SQLAlchemy(app)
jwt = JWTManager(app)
CORS(app, supports_credentials=True)
migrate = Migrate(app, db)
mail = Mail(app)
celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

# ✅ Configure Logging
logging.basicConfig(level=logging.INFO)

# ✅ Import Models and Routes after Initialization
from app.models import User, ServiceRequest
from app.api import initialize_routes
initialize_routes(app)

from app.models import db
# Initialize extensions
# db = SQLAlchemy(app)
# jwt = JWTManager(app)
# CORS(app, supports_credentials=True)
# db.init_app(app)
# migrate = Migrate(app, db)  # Bind Migrate with Flask app and db

migrate.init_app(app, db)
jwt.init_app(app)
from app.models import User
# from app.api import initialize_routes
# initialize_routes(app)
# from flask_mail import Mail
# mail = Mail
# Create the database
with app.app_context():
    db.create_all()
@celery.task(name="app.send_async_email")
def send_async_email(to_email, subject, body):
    """Send an email asynchronously using Flask-Mail"""
    try:
        msg = Message(subject, recipients=[to_email], body=body)
        mail.send(msg)
        logging.info(f"✅ Email sent successfully to {to_email}!")
        return f"✅ Email sent successfully to {to_email}!"
    except Exception as e:
        logging.error(f"❌ Email failed: {str(e)}")
        return f"❌ Email failed: {str(e)}"


@celery.task(name="app.send_async_email_csv")
def send_async_email_csv(to_email, subject, body, csv_attachment):
    """Send an email asynchronously with a CSV attachment using Flask-Mail"""
    try:
        msg = Message(subject, recipients=[to_email], body=body)
        msg.attach("completed_service_request.csv", "text/csv", csv_attachment)
        mail.send(msg)
        logging.info(f"✅ Email sent successfully to {to_email}!")
        return f"✅ Email sent successfully to {to_email}!"
    except Exception as e:
        logging.error(f"❌ Email failed: {str(e)}")
        return f"❌ Email failed: {str(e)}"


@app.route('/job', methods=['GET'])
def export_completed_request():
    """Exports completed service requests as a CSV and emails it to all admins."""
    completed_requests = ServiceRequest.query.filter_by(req_status='Closed').all()

    # ✅ Prepare CSV file in memory
    output_buffer = io.StringIO()
    fieldnames = [
        'service_req_id', 'service_id', 'customer_id', 'service_professional_id',
        'request_date', 'completion_date', 'status', 'remarks', 'address', 'pincode'
    ]
    csv_writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
    csv_writer.writeheader()

    for request in completed_requests:
        csv_writer.writerow({
            'service_req_id': request.service_req_id,
            'service_id': request.service_id,
            'customer_id': request.cust_id,
            'service_professional_id': request.service_pro_id,
            'request_date': request.req_action_date.strftime('%Y-%m-%d %H:%M:%S'),
            'completion_date': request.req_completed_date.strftime('%Y-%m-%d %H:%M:%S') if request.req_completed_date else 'N/A',
            'status': request.req_status,
            'remarks': request.req_remarks or 'N/A',
            'address': request.req_cust.user_address,
            'pincode': request.req_cust.user_pincode,
        })

    # ✅ Retrieve CSV content
    csv_data = output_buffer.getvalue()
    output_buffer.close()

    # ✅ Fetch all admin users
    admin_users = User.query.filter_by(user_role='admin').all()

    # ✅ Send CSV file via email to each admin
    email_subject = 'EasyEquity: Completed Service Requests Export'
    email_body = "Attached is the latest export of completed service requests."
    
    for admin in admin_users:
        send_async_email_csv.delay(admin.user_email, email_subject, email_body, csv_data)

    return jsonify({"message": "CSV export job has been triggered!"}), 202



if __name__ == '__main__':
    app.run(debug=True)


# import logging
# from flask import Flask
# from flask_mail import Mail, Message
# from celery import Celery
# # from run import app
# # from flask import current_app
# # Initialize Flask App
# app = Flask(__name__)
# # app = current_app
# # ✅ Flask-Mail Configuration for Outlook SMTP
# app.config['MAIL_SERVER'] = 'smtp.gmail.com'  # Outlook SMTP server
# app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_TLS'] = True
# app.config['MAIL_USE_SSL'] = False
# app.config['MAIL_USERNAME'] = 'easyequity01@gmail.com'  # Your Outlook email
# app.config['MAIL_PASSWORD'] = 'wcmdmwlnuhdbnryp'  # 🔥 Use an App Password
# # app.config['MAIL_DEFAULT_SENDER'] = ('EasyEquity', 'easyequity01@outlook.com')
# # app.config['MAIL_DEFAULT_SENDER'] = 'easyequity01@outlook.com'
# app.config['MAIL_DEFAULT_SENDER'] = 'easyequity01@gmail.com'

# # ✅ Celery Configuration (Redis as Broker & Backend)
# app.config['CELERY_BROKER_URL'] = 'redis://localhost:6369/0'
# app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6369/0'
# import socket
# app.config['MAIL_HELO_HOSTNAME'] = socket.gethostname()

# # ✅ Initialize Flask-Mail & Celery
# mail = Mail(app)
# celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
# celery.conf.update(app.config)

# # ✅ Configure Logging
# logging.basicConfig(level=logging.INFO)


# @celery.task(name="app.send_async_email")
# def send_async_email(to_email, subject, body):
#     """Send an email asynchronously using Flask-Mail"""
#     try:
#         with app.app_context():  # Ensures Flask context is available inside Celery
#             msg = Message(subject, recipients=[to_email], body=body)
#             mail.send(msg)
#             logging.info(f"✅ Email sent successfully to {to_email}!")
#             return f"✅ Email sent successfully to {to_email}!"
#     except Exception as e:
#         logging.error(f"❌ Email failed: {str(e)}")
#         return f"❌ Email failed: {str(e)}"


# @celery.task(name="app.send_async_email")
# def send_async_email_doc(to_email, subject, body, pdf_attachment ):
#     """Send an email asynchronously using Flask-Mail"""
#     try:
#         with app.app_context():  # Ensures Flask context is available inside Celery
#             msg = Message(subject, recipients=[to_email], body=body)
#             msg.attach("monthly_report.pdf", "application/pdf", pdf_attachment)
#             mail.send(msg)
#             logging.info(f"✅ Email sent successfully to {to_email}!")
#             return f"✅ Email sent successfully to {to_email}!"
#     except Exception as e:
#         logging.error(f"❌ Email failed: {str(e)}")
#         return f"❌ Email failed: {str(e)}"




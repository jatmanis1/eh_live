from .celery import celery
from flask import current_app
from ..models import ServiceRequest, User
from run import send_async_email, send_async_email_doc

@celery.task
def daily_reminder_professionals():
    from run import app  # Ensure app is imported
    with app.app_context():  # Ensure context is set
        pros = User.query.filter_by(user_role='pro').all()
        for pro in pros:
            pending_requests = ServiceRequest.query.filter(
                ServiceRequest.req_pro.has(id=pro.id), 
                ServiceRequest.req_status == "Pending"
            ).count()
            if pending_requests > 0:
                message = f"Reminder: You have {pending_requests} pending service requests. Please review them."
                send_async_email(pro.user_email, "Service Reminder", message)

from .celery import celery
from flask import render_template
import weasyprint
from datetime import datetime
from ..models import ServiceRequest, User
# from .mail import send_async_email_doc
from run import send_async_email, send_async_email_doc

from run import app  # Import `app` explicitly to use `app.app_context()`

@celery.task
def monthly_report_customer():
    with app.app_context():  # Ensure Flask app context is available
        now = datetime.now()
        month, year = now.month, now.year
        previous_month = month - 1 if month > 1 else 12
        previous_year = year if month > 1 else year - 1

        subject = 'EasyHome: Monthly Report For Your Account'

        custs = User.query.filter_by(user_role='cust').all()
        print(f"Found {len(custs)} customers")

        for customer in custs:
            c_id = customer.id
            reqs = ServiceRequest.query.filter(
                ServiceRequest.req_cust_id == c_id,
                ServiceRequest.req_action_date != None
            ).all()

            service_requests = [
                request for request in reqs
                # if request.req_action_date.month == previous_month and request.req_action_date.year == previous_year
            ]

            if service_requests:
                formatted_month = datetime(previous_year, previous_month, 1).strftime('%B')

                # Use Flask template rendering for better formatting
                report_html = render_template(
                    "monthly_report.html",
                    service_requests=service_requests,
                    customer=customer,
                    month=formatted_month,
                    year=previous_year
                )

                pdf = weasyprint.HTML(string=report_html).write_pdf()

                body = f"Dear {customer.user_name},\n\nPlease find your monthly report attached."

                send_async_email_doc(customer.user_email, subject, body, pdf)


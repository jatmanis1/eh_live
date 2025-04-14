# import csv
# import io
# from flask import render_template
# # from .celery import celery
# # from .template import send_email_with_csv
# from run import send_async_email_csv


# # @celery.task
# def export_completed_requests():
#     """Exports completed service requests as a CSV and emails it to all admins."""
    
#     from ..models import ServiceRequest, User  # Import inside function to avoid circular dependency
    
#     # Fetch completed service requests
#     completed_requests = ServiceRequest.query.filter_by(req_status='Closed').all()
    
#     # CSV file setup
#     output_buffer = io.StringIO()
#     fieldnames = [
#         'service_req_id', 'service_id', 'customer_id', 'service_professional_id',
#         'request_date', 'completion_date', 'status', 'remarks', 'address', 'pincode'
#     ]
    
#     csv_writer = csv.DictWriter(output_buffer, fieldnames=fieldnames)
#     csv_writer.writeheader()
    
#     for request in completed_requests:
#         csv_writer.writerow({
#             'service_request_id': request.service_req_id,
#             'service_id': request.service_id,
#             'customer_id': request.cust_id,
#             'service_professional_id': request.service_pro_id,
#             'request_date': request.req_action_date.strftime('%Y-%m-%d %H:%M:%S'),
#             'completion_date': request.req_completed_date.strftime('%Y-%m-%d %H:%M:%S') if request.req_completed_date else 'N/A',
#             'status': request.req_status,
#             'remarks': request.req_remarks or 'N/A',
#             'address': request.req_cust.user_address,
#             'pincode': request.req_cust.user_pincode,
#         })
    
#     # Retrieve CSV content
#     csv_data = output_buffer.getvalue()
#     output_buffer.close()
    
#     # Email content setup
#     email_subject = 'HomeMate: Completed Service Requests Export'
#     email_body = render_template('csv_export.html')
    
#     # Fetch all admin users
#     admin_users = User.query.filter_by(user_role='admin').all()
    
#     # Send CSV file via email to each admin
#     for admin in admin_users:
#         send_async_email_csv(admin.user_email, email_subject, email_body, csv_data)

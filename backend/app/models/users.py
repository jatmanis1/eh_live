from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta, timezone
from flask_jwt_extended import create_access_token
from sqlalchemy import func

db = SQLAlchemy()

class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String, nullable=False)
    user_username = db.Column(db.String, unique=True, nullable=False)
    user_password = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, unique=True, nullable=False)
    user_address = db.Column(db.String, nullable=False)
    user_pincode = db.Column(db.String(6), nullable=False)
    user_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    user_service = db.Column(db.Integer, db.ForeignKey('services.id', ondelete="SET NULL"), nullable=True)
    user_exp = db.Column(db.String, nullable=True)
    user_desc = db.Column(db.String, nullable=True)
    user_status = db.Column(db.String, nullable=True, default='unblocked')
    is_verified = db.Column(db.Boolean, default=0)
    user_rating = db.Column(db.Float, default=0, nullable=False)
    user_role = db.Column(db.String, nullable=False)

    # Relationship with Services table
    service = db.relationship('Services', backref=db.backref('users', lazy=True))

    def __init__(self, user_name, user_username, user_password, user_email, user_address, user_pincode, user_service=None, user_exp=None, user_desc=None, user_status="unblocked", user_role='cust', is_verified=False):
        self.user_name = user_name.capitalize()
        self.user_username = user_username
        self.user_email = user_email
        self.user_password = generate_password_hash(user_password, method='pbkdf2:sha256')
        self.user_address = user_address
        self.user_pincode = user_pincode
        self.user_date = datetime.utcnow()
        self.user_service = user_service
        self.user_exp = user_exp
        self.user_desc = user_desc
        self.user_rating = 0
        self.user_status = user_status
        self.user_role = user_role
        self.is_verified = is_verified

    def check_pass(self, password):
        return check_password_hash(self.user_password, password)

    def generate_token(self):
        return create_access_token(identity=str(self.id), expires_delta=timedelta(hours=2))

    def service_name(self):
        return self.service.to_dict()['service_name'] if self.service else None

    def update_rating(self):
        """ Updates the professional's average rating from service requests. """
        avg_rating = db.session.query(func.avg(ServiceRequest.req_rating)).filter(
            ServiceRequest.req_pro_id == self.id,
            ServiceRequest.req_rating.isnot(None)
        ).scalar()

        self.user_rating = round(avg_rating, 2) if avg_rating is not None else 0
        db.session.commit()  # Commit the updated rating

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.user_username,
            'name': self.user_name,
            'email': self.user_email,
            'user_role': self.user_role,
            'user_service': self.service_name(),
            'user_service_id': self.user_service,
            'user_desc': self.user_desc,
            'user_rating': self.user_rating,
            'user_status': self.user_status,
            'is_verified': self.is_verified,
            'user_exp': self.user_exp,
            'user_pincode': self.user_pincode,
            'user_address': self.user_address,
            'user_date': self.user_date.isoformat() if self.user_date else None,
        }


class Services(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(50), nullable=False)
    service_desc = db.Column(db.String(200))
    service_b_price = db.Column(db.Float, nullable=False)
    time_required = db.Column(db.String, nullable=False)

    def __init__(self, service_name, service_desc, service_b_price, time_required):
        self.service_name = service_name.capitalize()
        self.service_desc = service_desc
        self.service_b_price = service_b_price
        self.time_required = time_required

    def to_dict(self):
        return {
            "id": self.id,
            'service_name': self.service_name,
            'service_desc': self.service_desc,
            'service_b_price': self.service_b_price,
            'time_required': self.time_required,
        }


class ServiceRequest(db.Model):
    __tablename__ = 'service_requests'

    id = db.Column(db.Integer, primary_key=True)
    req_service_id = db.Column(db.Integer, db.ForeignKey('services.id', ondelete="SET NULL"), nullable=False)
    req_cust_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="SET NULL"), nullable=False)
    req_pro_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="SET NULL"), nullable=True)
    req_date = db.Column(db.Date, nullable=False, default=datetime.now(timezone.utc).date())
    req_req_date = db.Column(db.Date, nullable=True)
    req_status = db.Column(db.String(50), nullable=False, default="Pending")
    req_action_date = db.Column(db.Date, nullable=True)
    req_completed_date = db.Column(db.Date, nullable=True)
    req_rating = db.Column(db.Float, nullable=True)
    req_remark = db.Column(db.String(500), nullable=True)

    req_pro = db.relationship('User', foreign_keys=[req_pro_id], backref=db.backref('provider_requests', lazy=True))
    req_cust = db.relationship('User', foreign_keys=[req_cust_id], backref=db.backref('customer_requests', lazy=True))
    req_service = db.relationship('Services', backref=db.backref('service_requests', lazy=True))

    def __init__(self, req_service_id, req_cust_id, req_status="Pending", req_pro_id=None):
        self.req_service_id = req_service_id
        self.req_cust_id = req_cust_id
        self.req_pro_id = req_pro_id
        self.req_status = req_status
        self.req_date = datetime.now(timezone.utc).date()
        self.req_action_date = None
        self.req_completed_date = None
        self.req_rating = None
        self.req_remark = None

        if self.req_pro_id is None:
            self.req_status = 'Not Pro accepted yet'

    def update_status(self, status):
        """ Updates service request status and professional rating if completed. """
        self.req_status = status
        if status == "Closed":
            self.req_completed_date = datetime.now(timezone.utc).date()
        else:
            self.req_action_date = datetime.now(timezone.utc).date()

        if self.req_pro:
            self.req_pro.update_rating()

    def add_rating_and_remark(self, rating, remark):
        """ Adds rating and remark for the professional and updates their rating. """
        self.req_rating = rating
        self.req_remark = remark

        if self.req_pro:
            self.req_pro.update_rating()

    def to_dict(self):
        return {
            "id": self.id,
            "req_status": self.req_status,
            "req_cust_id": self.req_cust_id,
            "req_pro_id": self.req_pro_id,
            "req_service_id": self.req_service_id,
            "cust": self.req_cust.to_dict(),
            "pro": self.req_pro.to_dict() if self.req_pro else None,
            "service": self.req_service.to_dict(),
            "req_date": self.req_date.isoformat() if self.req_date else None,
            "req_action_date": self.req_action_date.isoformat() if self.req_action_date else None,
            "req_completed_date": self.req_completed_date.isoformat() if self.req_completed_date else None,
            "req_rating": self.req_rating,
            "req_remark": self.req_remark
        }

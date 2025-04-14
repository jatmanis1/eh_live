from . import db



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

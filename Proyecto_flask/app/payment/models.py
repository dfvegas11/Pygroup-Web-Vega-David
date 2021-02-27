from app.db import db, ma


class Payments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bank = db.Column(db.String(100))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class PaymentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Payments
        fields = ["id", "bank", "user_id"]

def get_all_payments():
    payments_qs = Payments.query.all()
    payment_schema = PaymentsSchema()
    payments_serialization = [payment_schema.dump(payment) for payment in payments_qs]

    return payments_serialization
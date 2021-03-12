from flask import Blueprint, Response, request, render_template, redirect, url_for, flash
from app.payment.forms import AddPaymentForm
from app.db import db
from app.payment.models import Payments
from flask_login import current_user, login_required

payment = Blueprint("payment", __name__, url_prefix="/payment")

@payment.route('/add-payment-method', methods=['GET', 'POST'])
@login_required
def add_payment_form():

    """
        Add payment method
        ---
        tags:
            - Payment
        description: Register a new form of payment in the DB for the logged in user
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    form_payment = AddPaymentForm()
    if request.method == 'POST' and form_payment.validate():
        new_payment = Payments(id=form_payment.id.data, bank=form_payment.bank.data, user_id=current_user.id)
        db.session.add(new_payment)
        db.session.commit()
        return redirect(url_for('products.show_products_catalog'))
    return render_template('add_payment_form.html', form=form_payment)
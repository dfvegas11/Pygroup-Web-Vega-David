from flask import Blueprint, Response, request, render_template, redirect, url_for, flash
from flask_login import login_required, current_user

car = Blueprint("car", __name__, url_prefix="/car")

@car.route('/shopping-car', methods=['GET'])
@login_required
def show_shopping_car():

    """
        Add product at shopping car
        ---
        tags:
            - Shopping
        description: Allows to see the products added in the shopping car and calculate the total and subtotal
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    my_info = {"name": current_user.name, "email": current_user.email}
    return render_template('shopping.html', my_info=my_info)
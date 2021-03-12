from flask import Blueprint, Response, request, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_manager, login_user, logout_user, login_required, current_user

from app.db import db
from app.auth.models import User
from app.payment.models import get_all_payments

auth = Blueprint("auth", __name__, url_prefix="/")

@auth.route("/", methods=['GET','POST'])
def login():

    """
        Login
        ---
        tags:
            - Auth
        description: Page for login of the users
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        remember = True if request.form.get("remember") else False

        user = User.query.filter_by(email=email).first()
        """ Checks if user does not exists in DB or if the password is 
        invalid. Redirects to login and shows error if this happens."""
        if not user or not check_password_hash(user.password, password):
            flash("Please check your login details and try again.")
            return redirect(url_for("auth.login"))

        login_user(user, remember=remember)
        return redirect(url_for("products.show_products_catalog"))
    return render_template('login.html')

@auth.route("/logout")
def logout():

    """
        Logout
        ---
        tags:
            - Auth
        description: finish the user session
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """
    
    logout_user()
    return redirect(url_for("auth.login"))

@auth.route("/signup", methods=['GET','POST'])
def signup():

    """
        Singup
        ---
        tags:
            - Auth
        description: Register a new user in the DB
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    if request.method == "POST":
        email = request.form.get("email")
        name = request.form.get("name")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        """If user exists shows an error and redirects to signup to try
        with other user.
        """
        if user:
            flash("Email address already exists")
            return redirect(url_for("auth.signup"))

        """Creates new user in DB with hashed password for security reasons"""
        new_user = User(email=email, name=name, password=generate_password_hash(password))

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth.login"))
    return render_template('signup.html')

@auth.route('/my-profile', methods=['GET'])
@login_required
def show_my_profile():

    """
        Show my profile
        ---
        tags:
            - Auth
        description: Allows to see all the data of the user and your payments methods
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    payment = get_all_payments()
    my_info = {"payments": payment, "name": current_user.name, "email": current_user.email, "id": current_user.id}
    return render_template('myProfile.html', my_info=my_info)
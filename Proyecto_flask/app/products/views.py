import sys
from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect, url_for
from app.products.forms import CreateCategoryForm
from app.products.models import (
    get_all_categories,
    create_new_category,
    get_all_products,
    get_product_by_id,
    create_new_product,
    create_new_Stock,
    get_stock_by_product,
    check_stock,
    get_stock,
    update_stock
)

products = Blueprint("products", __name__, url_prefix="/products")

EMPTY_SHELVE_TEXT = "Empty shelve!"
PRODUCTS_TITLE = "<h1> Products </h1>"
DUMMY_TEXT = "Dummy method to show how Response works"
RESPONSE_BODY = {"message": "", "data": [], "errors": [], "metadata": []}


@products.route("/dummy-product", methods=["GET", "POST"])
def dummy_product():
    """This method test the request types. If is GET Type it will
    render the text Products in h1 label with code 500.
    If is POST Type it will return Empty shelve! with status code 403
    """
    if request.method == "POST":
        return EMPTY_SHELVE_TEXT, HTTPStatus.FORBIDDEN

    return PRODUCTS_TITLE, HTTPStatus.INTERNAL_SERVER_ERROR


@products.route("/dummy-product-2")
def dummy_product_two():
    """This method shows how Response object could be used to make API
    methods.
    """
    return Response(DUMMY_TEXT, status=HTTPStatus.OK)


@products.route("/categories")
def get_categories():
    """
        Verificar que si get_all_categories es [] 400, message = "No hay nada"
    :return:
    """
    categories = get_all_categories()
    status_code = HTTPStatus.OK

    if categories:
        RESPONSE_BODY["message"] = "OK. Categories List"
        RESPONSE_BODY["data"] = categories
    else:
        RESPONSE_BODY["message"] = "OK. No categories found"
        RESPONSE_BODY["data"] = categories
        status_code = HTTPStatus.NOT_FOUND

    return RESPONSE_BODY, status_code


@products.route("/add-category", methods=["POST"])
def create_category():
    """

    :return:
    """
    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        category = create_new_category(data["name"])
        RESPONSE_BODY["message"] = "OK. Category created!"
        RESPONSE_BODY["data"] = category
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code

@products.route("/add-products", methods=['POST'])
def create_product():

    RESPONSE_BODY["message"] = "Method not allowed"
    status_code = HTTPStatus.METHOD_NOT_ALLOWED
    if request.method == "POST":
        data = request.json
        product = create_new_product(data["name"], data["price"], data["description"], data["category_id"])
        RESPONSE_BODY["message"] = "OK. Product created!"
        RESPONSE_BODY["data"] = product
        status_code = HTTPStatus.CREATED

    return RESPONSE_BODY, status_code

@products.route("/")
def get_products():
    products_obj = get_all_products()

    RESPONSE_BODY["data"] = products_obj
    RESPONSE_BODY["message"] = "Products list"

    return RESPONSE_BODY, 200


@products.route("/product/<int:id>")
def get_product(id):
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/product-stock/<int:product_id>")
def get_product_stock(product_id):
    product_stock = get_stock_by_product(product_id)
    RESPONSE_BODY["message"] = "Product stock"
    RESPONSE_BODY["data"] = product_stock

    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/need-restock")
def get_products_that_need_restock():
    products_low_stock = get_products_with_low_stock()
    RESPONSE_BODY["message"] = "This products need to be re-stocked"
    RESPONSE_BODY["data"] = products_low_stock

    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/register-product-stock/<int:id>", methods=["PUT", "POST"])
def register_product_refund_in_stock(id):

    # TODO Complete this view to update stock for product when a register for
    # this products exists. If not create the new register in DB

    status_code = HTTPStatus.CREATED
    if request.method == "PUT":
        data = request.json
        stock = update_stock(id, data["quantity"])
        RESPONSE_BODY["message"] = "Stock for this product were updated successfully!"
        RESPONSE_BODY["data"] = stock
        status_code = HTTPStatus.OK
        return RESPONSE_BODY, status_code
    elif request.method == "POST":
        if check_stock(id)==True:
            data = request.json
            stock = create_new_Stock(id, data["quantity"])
            RESPONSE_BODY["message"] = "Stock for this product were created successfully!"
            RESPONSE_BODY["data"] = stock
            status_code = HTTPStatus.CREATED
            return RESPONSE_BODY, status_code
        RESPONSE_BODY["message"] = "Stock for this product has been already created!"
        status_code = HTTPStatus.CREATED
        print (get_stock(id))
        return RESPONSE_BODY, status_code
    else:
        RESPONSE_BODY["message"] = "Method not Allowed"
        status_code = HTTPStatus.METHOD_NOT_ALLOWED
        return RESPONSE_BODY, status_code

@products.route('/success')
def success():
    return render_template('category_success.html')

@products.route('/create-category-form', methods=['GET', 'POST'])
def create_category_form():
    form_category = CreateCategoryForm()
    if request.method == 'POST' and form_category.validate():
        create_new_category(name=form_category.name.data)
        return redirect(url_for('products.success'))

    return render_template('create_category_form.html', form=form_category)

""" TAREA VISTAS
name = Blueprint('name',__name__,url_prefix='/name')
@name.route('/<name>', methods=['GET'])
def index(name):
    if name!="pygroup":
        return Response ("Felicitaciones! Trabajo exitoso {}".format(name), status=200)
    return Response ("ERROR! No se puede usar el nombre pygroup", status=400)
"""
"""Flask te permite usar plantillas para el contenido dinámico de páginas web.
Una de las cosas más sencillas que se pueden hacer en Flask es crear una página web ante una petición. 
Es decir, usar un template en Flask que sea una página HTML a la cual 
podemos insertar contenido recuperado desde nuestro programa Python.
A este método debemos pasarle el nombre de nuestra plantilla y las variables
necesarias para su renderizado como parámetros clave-valor."""


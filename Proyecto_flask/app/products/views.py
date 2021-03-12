import sys
from http import HTTPStatus
from flask import Blueprint, Response, request, render_template, redirect, url_for
from app.products.forms import CreateCategoryForm, CreateProductForm
from flask_login import login_required
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

@products.route("/categories")
def get_categories():
    """
        List all categories
        ---
        tags:
            - Products
        description: Allows to see all the categories in the BD
        responses:
            400:
                description: No category found
            200:
                description: Ok

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
        Add categories
        ---
        tags:
            - Products
        description: Method for add categories in the BD
        responses:
            405:
                description: Method not allowed
            200:
                description: Ok

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

    """
        Add products
        ---
        tags:
            - Products
        description: Method for add products in the BD
        responses:
            405:
                description: Method not allowed
            200:
                description: Ok

    """

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

    """
        List all products
        ---
        tags:
            - Products
        description: Allows to see all the products in the BD
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed

    """

    products_obj = get_all_products()

    RESPONSE_BODY["data"] = products_obj
    RESPONSE_BODY["message"] = "Products list"

    return RESPONSE_BODY, 200


@products.route("/product/<int:id>")
def get_product(id):
    """
    Shows the info of the products filtering by id

    ---
    tags:
        - Products
    parameters:
        - in: path
            name:id
            description:Product ID
            type:integer
    responses:
        200:
            description: OK
        500:
            description: Product not found
        405:
            description: Method not allowed
    """
    product = get_product_by_id(id)

    RESPONSE_BODY["data"] = product
    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/product-stock/<int:product_id>")
def get_product_stock(product_id):

    """
    Shows the stock of the products filtering by id

    ---
    tags:
        - Products
    parameters:
        - in: path
            name:id
            description:Product ID
            type:integer
    responses:
        200:
            description: OK
        500:
            description: Product not found
        405:
            description: Method not allowed
    """

    product_stock = get_stock_by_product(product_id)
    RESPONSE_BODY["message"] = "Product stock"
    RESPONSE_BODY["data"] = product_stock

    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/need-restock")
def get_products_that_need_restock():
    
    """
        List all products that need restock 
        ---
        tags:
            - Products
        description: Allows to see all the products that need restock in the BD
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    products_low_stock = get_products_with_low_stock()
    RESPONSE_BODY["message"] = "This products need to be re-stocked"
    RESPONSE_BODY["data"] = products_low_stock

    return RESPONSE_BODY, HTTPStatus.OK


@products.route("/register-product-stock/<int:id>", methods=["PUT", "POST"])
def register_product_refund_in_stock(id):

    """
    Register the stock of the product filtering by id

    ---
    tags:
        - Products
    parameters:
        - in: path
            name:id
            description:Product ID
            type:integer
    responses:
        200:
            description: OK
        500:
            description: Product not found
        405:
            description: Method not allowed
    """

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
    """
        Category create correct
        ---
        tags:
            - Products
        description: Send a message if the new category is create correct
        responses:
            200:
                description: Ok
    """

    return render_template('category_success.html')

@products.route('/create-category-form', methods=['GET', 'POST'])
def create_category_form():

    """
        Create category form
        ---
        tags:
            - Products
        description: Create category with a form of Flask
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """
    
    form_category = CreateCategoryForm()
    if request.method == 'POST' and form_category.validate():
        create_new_category(name=form_category.name.data)
        return redirect(url_for('products.success'))

    return render_template('create_category_form.html', form=form_category)

@products.route('/success_product')
def success_product():

    """
        Product create correct
        ---
        tags:
            - Products
        description: Send a message if the new product is create correct
        responses:
            200:
                description: Ok
    """

    return render_template('product_success.html')

@products.route('/create-product-form', methods=['GET', 'POST'])
def create_product_form():

    """
        Create product form
        ---
        tags:
            - Products
        description: Create product with a form of Flask
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    form_product = CreateProductForm()
    if request.method == 'POST' and form_product.validate():
        create_new_product(name=form_product.name.data, price=form_product.price.data, description=form_product.description.data, category_id=form_product.category_id.data)
        return redirect(url_for('products.success_product'))

    return render_template('create_product_form.html', form=form_product)

@products.route('/add-category-old', methods=['GET', 'POST'])
def create_category_old():

    """
        Create category with old way
        ---
        tags:
            - Products
        description: Create category with a form HTML
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """
    
    if request.method=='POST':
        category = create_new_category(request.form["name"])
        RESPONSE_BODY["message"] = "Se agrego la categoria {} con exito".format(request.form["name"])
        RESPONSE_BODY["data"] = category
        status_code = HTTPStatus.CREATED
        return RESPONSE_BODY, status_code
    return render_template("form_category_old.html")

@products.route('/add-product-old', methods=['GET', 'POST'])
def create_product_old():

    """
        Create product with old way
        ---
        tags:
            - Products
        description: Create product with a form HTML
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    if request.method=='POST':
        product = create_new_product(request.form["name"],request.form["price"],request.form["description"],request.form["category_id"])
        RESPONSE_BODY["message"] = "Se agrego el pructo {} con exito".format(request.form["name"])
        RESPONSE_BODY["data"] = product
        status_code = HTTPStatus.CREATED
        return RESPONSE_BODY, status_code
    return render_template("form_product_old.html")

@products.route('/show-catalog', methods=['GET'])
@login_required
def show_products_catalog():

    """
        Show catalog
        ---
        tags:
            - Products
        description: Allows to see all the products in the BD
        responses:
            200:
                description: Ok
            405:
                description: Method not allowed
    """

    products = get_all_products()
    my_info = {"products": products, "pygroup": "Pygroup 2020"}
    return render_template('catalog.html', my_info=my_info)

@products.route('/temp')
def temp():
    return render_template('child1.html')


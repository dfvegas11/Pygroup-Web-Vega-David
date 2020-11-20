from datetime import datetime

from flask import jsonify

from app.db import db, ma


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    image =db.Column(db.String(500), default="https://bit.ly/3loPYXP")
    price = db.Column(db.Integer, nullable=False)
    weight = db.Column(db.Integer, default=1)
    description = db.Column(db.String(500), nullable=True)
    refundable = db.Column(db.Boolean, default=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


class ProductSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Product
        fields = ["id", "name", "price","category_id"]


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category


class Stock(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
    quantity = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    updated_at = db.Column(db.DateTime, default=datetime.now())

class StockSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Stock
        


def get_all_categories():
    categories = Category.query.all()
    category_schema = CategorySchema()
    categories = [category_schema.dump(category) for category in categories]
    return categories


def create_new_category(name):
    category = Category(name=name)
    db.session.add(category)

    if db.session.commit():
        return category

    return None

def create_new_product(name, price, description, category_id):
    """
    
    """
    product = Product(name=name,price=price,description=description,category_id=category_id)
    db.session.add(product)

    if db.session.commit():
        return product
    return None

def get_all_products():
    products_qs = Product.query.all()
    product_schema = ProductSchema()
    products_serialization = [product_schema.dump(product) for product in products_qs]

    return products_serialization


def get_product_by_id(id):
    product_qs = Product.query.filter_by(id=id).first()
    product_schema = ProductSchema()
    p = product_schema.dump(product_qs)
    return p

def create_new_Stock(product_id, quantity):
    """
    
    """
    stock = Stock(product_id=product_id, quantity=quantity)
    db.session.add(stock)

    if db.session.commit():
        return stock
    return None

def get_stock_by_product(product_id):
    product_Stock = Stock.query.filter_by(product_id=product_id).first()
    stock_schema = StockSchema()
    s = stock_schema.dump(product_Stock)
    return s

def check_stock (product_id):
    product_Stock = Stock.query.filter_by(product_id=product_id).first()
    if product_Stock.quantity is None:
        return True
    return False

def get_stock(product_id):
    product_Stock = Stock.query.filter_by(product_id=product_id).first()
    return product_Stock.quantity

def update_stock(product_id,quantity):
    product_Stock = Stock.query.filter_by(product_id=product_id).first()
    suma = product_Stock.quantity+int(quantity)
    product_Stock.quantity = suma
    db.session.commit()
    return suma
from flask import Flask, Response
from products.views import prod

app = Flask(__name__)
app.register_blueprint(prod)

if __name__ == "__main__":
    app.run(debug=True)

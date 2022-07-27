from flask import Flask
from flask_restful import Api

from db import db

app = Flask(__name__)
api = Api(app)

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = 'sk'


@app.before_first_request
def create_tables():
    db.create_all()


# Test view
@app.route('/')
def home():
    return "It's working!"


if __name__ == '__main__':
    app.run(debug=True)

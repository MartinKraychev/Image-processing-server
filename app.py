import os

from flask import Flask
from flask_restful import Api

from db import db
from resources.original_img import UploadImage
from dotenv import load_dotenv

# Create .env file and have DATABASE_URL and SECRET_KEY variables in it
# This command loads the variables
load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config['PROPAGATE_EXCEPTIONS'] = True
# DATABASE_URL should follow this pattern for Postgre: postgresql://{username}:{password}@{host}:{port}/{db_name}
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
app.secret_key = os.getenv('SECRET_KEY')


api.add_resource(UploadImage, '/upload')


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

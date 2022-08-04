import os

import cloudinary
from dotenv import load_dotenv
from flask import Flask
from flask_restful import Api

from db import db
from resources.original_img import UploadImage
from resources.processed_img import GetImage

# Create .env file and have DATABASE_URL and SECRET_KEY variables in it
# This command loads the variables

load_dotenv()

app = Flask(__name__)
api = Api(app)

app.config["PROPAGATE_EXCEPTIONS"] = True
# DATABASE_URL should follow this pattern for Postgre: postgresql://{username}:{password}@{host}:{port}/{db_name}

uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)

app.config["SQLALCHEMY_DATABASE_URI"] = uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

app.secret_key = os.getenv("SECRET_KEY", "sk")

api.add_resource(UploadImage, "/images")
api.add_resource(GetImage, "/image/<string:img_id>")

cloudinary.config(
    cloud_name=os.getenv('CLOUD_NAME', 'dtxdbvgoo'),
    api_key=os.getenv('API_KEY', '795737877112786'),
    api_secret=os.getenv('API_SECRET', 'PKCT_vHBMJG71tn6xsaq4ROTPAM'))


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)

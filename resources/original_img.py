import os

from flask import request
from flask_restful import Resource, marshal
from werkzeug.utils import secure_filename

from models.original_img import OriginalImageModel
from resources.utils.file_helpers import check_allowed_file_type, check_file_size
from resources.utils.resource_fields import img_resource_field

save_folder = os.getenv('ORIGINAL_UPLOAD_FOLDER')


class UploadImage(Resource):

    @staticmethod
    def post():
        # Edge cases
        if 'file' not in request.files:
            return {'message': "Key parameter 'file' not provided"}, 400

        file = request.files['file']

        if not file or not check_allowed_file_type(file.filename):
            return {'message': 'Only pgn, jpeg, and jpg files are allowed'}, 400

        if not check_file_size(request.content_length):
            return {'message': 'Max size allowed is 1MB'}, 400
        # End of edge cases

        # Sanitize the name before storing it in the db
        filename = secure_filename(file.filename)
        file_path = os.path.join("./" + save_folder + filename)
        file.save(file_path)
        img = OriginalImageModel(filename=filename, path=save_folder+filename)
        img.save_to_db()

        return marshal(img, img_resource_field), 201

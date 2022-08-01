import json
from urllib.parse import urlsplit, parse_qsl

from flask import request
from flask_restful import Resource, marshal
from werkzeug.utils import secure_filename

from models.original_img import OriginalImageModel
from models.processed_img import ProcessedImageModel
from manipulations.img_processor import image_processor
from resources.utils.file_helpers import is_valid_uuid
from resources.utils.resource_fields import img_resource_field


# Example http://localhost:5000/image/<id>?resize={"height":300, "width":150}&flip={"code":1}&resize={"height":500, "width":1000}

class GetImage(Resource):
    @staticmethod
    def get(img_id):

        if not is_valid_uuid(img_id):
            return {'message': 'Invalid ID type'}, 400

        image = OriginalImageModel.query.filter_by(id=img_id).first()
        query = urlsplit(request.url).query

        if not image:
            return {'message': 'Image not found'}, 404

        if not query:
            return marshal(image, img_resource_field), 200

        cached_image = ProcessedImageModel.query.filter_by(params=query, original_img_id=img_id).first()

        if cached_image:
            return marshal(cached_image, img_resource_field), 200

        params_pairs = parse_qsl(query)
        parsed_pairs = []
        for item in params_pairs:
            parsed_pairs.append({item[0]: json.loads(item[1])})

        img_path, img_filename = image_processor(image.path, parsed_pairs)
        filename = secure_filename(img_filename)
        img = ProcessedImageModel(filename=filename, path=img_path+filename, params=query, original_img_id=img_id)
        img.save_to_db()

        return marshal(img, img_resource_field), 201

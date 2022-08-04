import json

from json import JSONDecodeError
from urllib.parse import urlsplit, parse_qsl

from flask import request
from flask_restful import Resource, marshal
from werkzeug.utils import secure_filename

from manipulations.img_processor import image_processor
from models.original_img import OriginalImageModel
from models.processed_img import ProcessedImageModel
from resources.utils.file_helpers import is_valid_uuid
from resources.utils.resource_fields import (
    original_img_resource_field,
    processed_img_resource_field,
)


# Example http://localhost:5000/image/<id>?resize={"height":300, "width":150}&flip={"code":1}&resize={"height":500, "width":1000}


class GetImage(Resource):
    """
    GET Endpoint by image id for processing images
    """

    @staticmethod
    def get(img_id):

        # Edge cases
        if not is_valid_uuid(img_id):
            return {"message": "Invalid ID type"}, 400

        image = OriginalImageModel.query.filter_by(id=img_id).first()
        query = urlsplit(request.url).query

        if not image:
            return {"message": "Image not found"}, 404

        if not query:
            return marshal(image, original_img_resource_field), 200

        cached_image = ProcessedImageModel.query.filter_by(
            params=query, original_img_id=img_id
        ).first()

        if cached_image:
            return marshal(cached_image, processed_img_resource_field), 200

        # Turns the query string into list of dictionaries
        params_pairs = parse_qsl(query)
        parsed_pairs = []
        try:
            for item in params_pairs:
                parsed_pairs.append({item[0]: json.loads(item[1])})
        except JSONDecodeError:
            return {"message": "Invalid json format"}, 400

        # Catch a raise from the manipulations module.
        try:
            img_path, img_filename = image_processor(image.path, parsed_pairs)
        except KeyError:
            return {
                "message": "Wrong key in the query parameters. Refer to the documentation for more details."
            }, 400
        except ValueError:
            return {
                "message": "Wrong value in the query parameters. Refer to the documentation for more details."
            }, 400
        # End of edge cases

        # Sanitizes the filename before it goes in the db
        filename = secure_filename(img_filename)

        # Saves the image location and name in the db
        img = ProcessedImageModel(
            filename=filename,
            path=img_path,
            params=query,
            original_img_id=img_id,
        )
        img.save_to_db()

        return marshal(img, processed_img_resource_field), 201

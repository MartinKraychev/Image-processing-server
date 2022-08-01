from flask_restful import fields

"""
Serializers for images
"""

original_img_resource_field = {
    'id': fields.String,
    'path': fields.String
}

processed_img_resource_field = {
    'id': fields.String,
    'path': fields.String,
    'original_img_id': fields.String
}

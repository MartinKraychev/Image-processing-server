from flask_restful import fields

img_resource_field = {
    "id": fields.String,
    "filename": fields.String,
    "path": fields.String,
}

import uuid

from sqlalchemy.dialects.postgresql import UUID

from db import db


class ProcessedImageModel(db.Model):
    __tablename__ = "processed_image"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = db.Column(db.String(100))
    path = db.Column(db.Text())
    params = db.Column(db.Text())
    original_img_id = db.Column(UUID, db.ForeignKey("original_image.id", ondelete="CASCADE"))

    def __init__(self, filename, path, params, original_img_id):
        self.filename = filename
        self.path = path
        self.params = params
        self.original_img_id = original_img_id

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

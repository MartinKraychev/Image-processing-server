import uuid

from sqlalchemy.dialects.postgresql import UUID

from db import db


class OriginalImageModel(db.Model):
    __tablename__ = "original_image"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    filename = db.Column(db.String(100))
    path = db.Column(db.Text())
    images = db.relationship("ProcessedImageModel", cascade="all, delete")

    def __init__(self, filename, path):
        self.filename = filename
        self.path = path

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

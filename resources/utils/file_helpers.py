import uuid

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
FILE_MAX_SIZE = 1 * 1000 * 1000


def check_allowed_file_type(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def check_file_size(size):
    return FILE_MAX_SIZE > size


def is_valid_uuid(val):
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

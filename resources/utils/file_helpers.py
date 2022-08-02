import uuid

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}
FILE_MAX_SIZE = 1 * 1000 * 1000


def check_allowed_file_type(filename):
    """
    Checks if the filename has an allowed extension type.
    """
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def check_file_size(size):
    """
    Checks if the file size is in the correct limits.
    """
    return FILE_MAX_SIZE > size


def is_valid_uuid(val):
    """
    Check if the given value is in correct uuid format.
    """
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False

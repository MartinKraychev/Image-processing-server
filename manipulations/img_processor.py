import os
import uuid

import cv2

import manipulations.img_manipulations as img_man


def image_processor(img_location, query_params):
    """
    Execute all image manipulations from the query parameters in the url, preserving the order.
    """
    src = cv2.imread(img_location)

    for el in query_params:
        for key, value in el.items():
            func = getattr(img_man, key)
            src = func(src, value)

    filename, extension = os.path.basename(img_location).split(".")
    new_filename = filename + f"-{uuid.uuid4()}." + extension
    save_folder = os.getenv('PROCESSED_UPLOAD_FOLDER')

    cv2.imwrite(os.path.abspath("./" + save_folder + new_filename), src)

    return save_folder, new_filename

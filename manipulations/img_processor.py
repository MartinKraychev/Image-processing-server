import os
import uuid

import cv2

from manipulations.img_manipulations import rotate, resize, crop, flip, grayscale


def image_processor(img_location, query_params):
    """
    Execute all image manipulations from the query parameters in the url, preserving the order.
    """
    mapper = {
        "rotate": rotate,
        "resize": resize,
        "crop": crop,
        "flip": flip,
        "grayscale": grayscale,
    }

    src = cv2.imread(img_location)

    for el in query_params:
        for key, value in el.items():
            if key in mapper:
                src = mapper[key](src, value)

    filename, extension = os.path.basename(img_location).split(".")
    new_filename = filename + f"-{uuid.uuid4()}." + extension
    save_folder = "/static/processed_images/"

    cv2.imwrite(os.path.abspath("./" + save_folder + new_filename), src)

    return save_folder, new_filename

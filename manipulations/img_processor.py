import os
import urllib.request
import uuid

import cloudinary.uploader
import cv2
import numpy as np

import manipulations.img_manipulations as img_man

SAVE_FOLDER = "processed_images"
TEMP_IMG_FOLDER = "/static/temp_images/"


def image_processor(img_location, query_params):
    """
    Execute all image manipulations from the query parameters in the url, preserving the order.
    """
    url_response = urllib.request.urlopen(img_location)
    src = cv2.imdecode(np.array(bytearray(url_response.read()), dtype=np.uint8), -1)

    for el in query_params:
        for key, value in el.items():
            func = getattr(img_man, key)
            src = func(src, value)

    filename, extension = os.path.basename(img_location).split(".")
    filename_uuid = filename + f"-{uuid.uuid4()}." + extension

    # Saves the img temporarily
    file_path = "./{}{}".format(TEMP_IMG_FOLDER, filename_uuid)
    cv2.imwrite(file_path, src)

    # Uploads the image to cloudinary
    upload_result = cloudinary.uploader.upload(file_path, folder=SAVE_FOLDER)

    # The image is now kept in the cloud and is no longer needed locally.
    # Removes the image
    os.remove(file_path)

    return upload_result["url"], filename_uuid

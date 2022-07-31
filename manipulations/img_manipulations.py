import cv2
import imutils

"""
Examples:
rotate - {'rotate':{angle:45}}
resize - {'resize':{'height':300,'width':300}}
crop - {'crop':{'height':300,'width':300}}
flip - {'flip':{'code':1}}
grayscale - {'grayscale':{}}
"""


# def rotate(src, angle):
#     height, width = src.shape[:2]
#     center = (width / 2, height / 2)
#
#     angle_to_int = int(angle['angle'])
#
#     rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=-angle_to_int, scale=1.0)
#
#     cos = np.abs(rotate_matrix[0, 0])
#     sin = np.abs(rotate_matrix[0, 1])
#
#     new_width = int((height * sin) + (width * cos))
#     new_height = int((height * cos) + (width * sin))
#
#     rotate_matrix[0, 2] += (new_width / 2) - center[0]
#     rotate_matrix[1, 2] += (new_height / 2) - center[1]
#
#     return cv2.warpAffine(src=src, M=rotate_matrix, dsize=(new_width, new_height))

def rotate(src, angle):
    """
    Rotate the NumPy array to 90, 180 or 270 degrees angle.
    """
    angle_to_int = int(angle['angle'])
    return imutils.rotate_bound(src, angle=angle_to_int)


def resize(src, dimensions):
    """
    Resize the NumPy array with the given dimensions.
    """
    height = int(dimensions['height'])
    width = int(dimensions['width'])

    return cv2.resize(src, (width, height), interpolation=cv2.INTER_AREA)


def crop(src, dimensions):
    """
    Crop the NumPy array with the given dimensions.
    """
    crop_height = int(dimensions['height'])
    crop_width = int(dimensions['width'])

    return src[0:crop_height, 0:crop_width]


def flip(src, flip_code):
    """
    Flip the NumPy array with the given code.

    flip_code = 0 - vertical flip
    flip_code = 1 - horizontal flip
    flip_code = -1 - vertical and horizontal flip
    """
    flip_code_int = int(flip_code['code'])

    return cv2.flip(src, flipCode=flip_code_int)


def grayscale(src, *args):
    """
    Convert the NumPy array from BGR to grayscale.
    *arg is not used, it's needed to provide the high abstraction level in img_processor.py
    """
    return cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

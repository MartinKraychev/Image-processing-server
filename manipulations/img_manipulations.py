import cv2
import imutils

"""
Examples:
rotate - {"rotate":{"angle":45}}
resize - {"resize":{"height":300,"width":300}}
crop - {"crop":{"height":300,"width":300}}
flip - {"flip":{"code":1}}
grayscale - {"grayscale":{}}
"""


def rotate(src, angle):
    """
    Rotate the NumPy array clockwise in multiples of 90 (90, 180 or 270) degrees angle.
    Rotating by arbitrary degrees is possible, but generates black borders that stack up on each rotate.
    """
    angle_to_int = int(angle["angle"])
    return imutils.rotate_bound(src, angle=angle_to_int)


def resize(src, dimensions):
    """
    Resize the NumPy array with the given dimensions.
    """
    height = int(dimensions["height"])
    width = int(dimensions["width"])

    return cv2.resize(src, (width, height), interpolation=cv2.INTER_AREA)


def crop(src, dimensions):
    """
    Slice the NumPy array with the given dimensions, starting from 0, 0 (top-left array corner).
    """
    height = int(dimensions["height"])
    width = int(dimensions["width"])

    return src[0:height, 0:width]


def flip(src, flip_code):
    """
    Flip the NumPy array with the given code.

    flip_code = 0 - flipping around the x-axis (vertical flip)
    flip_code = 1 - flipping around the y-axis (horizontal flip)
    flip_code = -1 - flipping around both axes (vertical and horizontal flip)
    """
    flip_code_to_int = int(flip_code["code"])

    return cv2.flip(src, flipCode=flip_code_to_int)


def grayscale(*args):
    """
    Convert the NumPy array from BGR to grayscale.
    """
    return cv2.cvtColor(args[0], cv2.COLOR_BGR2GRAY)

import cv2
import imutils
import numpy as np

"""
Examples:
rotate - {"rotate":{"angle":45}}
resize - {"resize":{"height":300,"width":300}}
crop - {"crop":{"height":300,"width":300}}
flip - {"flip":{"code":1}}
grayscale - {"grayscale":{}}
color_filter - {"color_filter":{"color":"red"}
"""


def rotate(src, angle):
    """
    Rotate the NumPy array clockwise in multiples of 90 (-90, 90, 180 or 270) degrees angle.
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


def color_filter(src, color):
    """
    Convert the NumPy array from BGR to grayscale.
    Using HSV range and masking, filter the color of interest and overlay the grayscale array with it.
    """
    hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    # Set the bounds for the red hue
    lower_red = np.array([160, 100, 50])
    upper_red = np.array([180, 255, 255])

    # Create a mask using the bounds set
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Create an inverse of the mask
    mask_inv = cv2.bitwise_not(mask)

    # Filter only the red colour from the original image using the mask (foreground)
    res = cv2.bitwise_and(src, src, mask=mask)

    # Filter the regions containing colours other than red from the grayscale image (background)
    background = cv2.bitwise_and(gray, gray, mask=mask_inv)

    # Convert the one channelled grayscale background to a three channelled image
    background = np.stack((background,) * 3, axis=-1)

    # Add the foreground and the background
    return cv2.add(res, background)

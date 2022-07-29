import json
from urllib.parse import parse_qs, urlparse
import cv2
import numpy as np
import re

"""

rotate - {'rotate':{angle:45}}
resize - {'resize':{'height':'300','width':'300'}}
crop - {'crop':{'height':'300','width':'300'}}
flip - {'flip':{'code':1}}
grayscale - {'grayscale':{'condition':'True'}}

"""

url = "http://www.example.org/image.jpg?option={rotate:{angle:45}}&option={flip:{code:1}}&option={rotate:{angle:45}}"
url2 = "http://www.example.org/image.jpg?option={'rotate':{'angle':45}}&option={'flip':{'code':1}}&option={'rotate':{'angle':45}}"

query = urlparse(url2).query
params = parse_qs(query)
print("params.values", params.values())


for value in params.values():
    for i in value:
        j = re.sub("'", "\"", i)
        print("j---------", j)
        str_to_dict = json.loads(j)
        print(str_to_dict)


def option_rotate(image_path: str, angle: int):
    src = cv2.imread(image_path)
    print("Original Dimensions : ", src.shape)

    height, width = src.shape[:2]
    center = (width / 2, height / 2)

    # using cv2.getRotationMatrix2D() to get the rotation matrix
    rotate_matrix = cv2.getRotationMatrix2D(center=center, angle=-angle, scale=1.0)

    cos = np.abs(rotate_matrix[0, 0])
    sin = np.abs(rotate_matrix[0, 1])

    new_width = int((height * sin) + (width * cos))
    new_height = int((height * cos) + (width * sin))

    rotate_matrix[0, 2] += (new_width / 2) - center[0]
    rotate_matrix[1, 2] += (new_height / 2) - center[1]

    # rotate the image using cv2.warpAffine
    rotated_image = cv2.warpAffine(src=src, M=rotate_matrix, dsize=(new_width, new_height))

    cv2.imshow("Rotated image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def option_resize(image_path: str, height: int, width: int):
    src = cv2.imread(image_path)
    print("Original Dimensions : ", src.shape)

    dim = (width, height)

    resized_img = cv2.resize(src, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow("Resized image", resized_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def option_crop(image_path: str, crop_height: int, crop_width: int):
    src = cv2.imread(image_path)
    print("Original Dimensions : ", src.shape)

    cropped_img = src[0:crop_height, 0:crop_width]

    cv2.imshow("Cropped Image", cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def option_grayscale(image_path: str):
    src = cv2.imread(image_path)
    print("Original Dimensions : ", src.shape)

    grayscale_image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Grayscale image", grayscale_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def option_flip(image_path: str, flip_code: int):
    src = cv2.imread(image_path)
    print("Original Dimensions : ", src.shape)

    """
    flip_code = 0 - vertically
    flip_code = 1 - horizontally
    flip_code = -1 - vertically and horizontally 
    """

    flipped_img = cv2.flip(src, flipCode=flip_code)

    cv2.imshow("Flipped Image", flipped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


mapper = {
    "rotate": "rotate",
}

# for key, value in params.items():
#     if key in mapper:
#         mapper[key]()

# option_resize("1.jpg", 300, 650)
# option_crop("1.jpg", 500, 200)
# option_rotate("1.jpg", 67)
# option_grayscale("1.jpg")
# option_flip("1.jpg", 1)
# rotate_bound("1.jpg", 45)

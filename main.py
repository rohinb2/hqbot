from hqbot import *

import time
import cv2

def get_image():
    retval, im = camera.read()
    return im

if __name__ == "__main__":
    camera = cv2.VideoCapture(0)
    for i in xrange(30):
        get_image()
    img = get_image()
    cv2.imwrite(os.path.join(os.path.dirname(__file__),"imgs/img.jpeg"),img)
    search("img.jpeg")

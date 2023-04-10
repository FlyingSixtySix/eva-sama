import cv2
import numpy as np


def rating(image, x1, y1, x2, y2):
    image = image.crop((x1, y1, x1+x2, y1+y2))
    image = np.array(image)
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    lower = np.array([0,0,0])
    upper = np.array([0,0,0])
    mask = cv2.inRange(hsv, lower, upper)
    image = 255 - mask
    rating = np.sum(image == 0)
    if rating == 0:
        return True
    else:
        return False
    

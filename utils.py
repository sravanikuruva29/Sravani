import cv2
import re
import numpy as np

def preprocess_plate(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    gray = cv2.resize(gray, None, fx=3, fy=3,
                      interpolation=cv2.INTER_CUBIC)

    gray = cv2.GaussianBlur(gray,(5,5),0)

    gray = cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return gray


def clean_plate(text):

    text = text.upper()
    text = re.sub(r'[^A-Z0-9]', '', text)

    text = text.replace("O","0")
    text = text.replace("I","1")
    text = text.replace("Z","2")

    return text


def valid_plate(text):

    if len(text) >= 7 and len(text) <= 11:
        return True

    return False
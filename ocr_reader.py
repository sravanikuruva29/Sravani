import easyocr

reader = easyocr.Reader(['en'])

def read_plate(image):

    result = reader.readtext(image)

    if len(result) > 0:
        text = result[0][1]
        return text

    return ""
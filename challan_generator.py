from reportlab.pdfgen import canvas

def generate_challan(plate,time,image):

    filename=f"challans/{plate}_{time}.pdf"

    c=canvas.Canvas(filename)

    c.drawString(100,750,"Traffic Violation Challan")

    c.drawString(100,700,f"Vehicle Number: {plate}")
    c.drawString(100,670,f"Violation: No Helmet")
    c.drawString(100,640,f"Time: {time}")
    c.drawString(100,610,"Fine Amount: ₹500")

    c.drawString(100,580,"Evidence Image Saved")

    c.save()

    return filename
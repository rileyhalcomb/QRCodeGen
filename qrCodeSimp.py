# import qrcode library
import qrcode as qr

data = ""

# creating the instance of QRCode class
qr.QRCode(version=1, error_correction=qr.constants.ERROR_CORRECT_H, box_size=10, border=4).make(data, fit=True)

# setting the image data
img = qr.make_image(fill_color="black", back_color="white")

# saving the image to the directory
img.save("qrcode.png")
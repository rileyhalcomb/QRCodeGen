# import qrcode library
import qrcode

# setting data
data = "https://github.com/rileyhalcomb/QRCodeGen"

# creating an instance of QRCode class
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)

# adding the data and making the qrcode
qr.add_data(data)

qr.make(fit=True)

# setting image data
img = qr.make_image(fill_color="black", back_color="white")

# saving the image to directory
img.save("qrcode.png")

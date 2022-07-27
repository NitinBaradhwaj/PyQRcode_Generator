import qrcode

input_URL = "https://www.youtube.com/"

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=2,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white", scale="5")
img.save("url_qrcode.png")

print(qr.data_list)
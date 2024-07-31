import qrcode

# Data to be encoded
data = input("Enter a argument. ")
# Encoding data using make() function
qr_img = qrcode.make(data)

# Saving as an image file
qr_img.save('MyQRCode1.png')

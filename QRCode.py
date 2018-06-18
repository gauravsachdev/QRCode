import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
#Encoding an alphanumeric code into a QRCode
#Size of the QR code to be generated
qr=qrcode.QRCode(version=1,box_size=10,border=4)
#Any alpha-numeric data can be added
#Unaware of the size limit but take 20 characters
#Can change the data within '' or even use a variable so can use input
qr.add_data('WB-324-R1934')
qr.make(fit=True)
#Creating the QR code
img=qr.make_image()
#The save location includes the filename and the extension
img.save('SAVE LOCATION')
#Decoding a QRCode
#Saved Location is the name of file with extension of the qr code
decoded=decode(Image.open('SAVED LOCATION'))
#This print statement will print the data you have added
print(str(decoded[0].data)[2:-1])

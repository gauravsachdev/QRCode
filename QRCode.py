import qrcode
from pyzbar.pyzbar import decode
from PIL import Image
#Encoding an alphanumeric code into a QRCode
qr=qrcode.QRCode(version=1,box_size=10,border=4)
qr.add_data('WB-324-R1934')
qr.make(fit=True)
img=qr.make_image()
img.save('SAVE LOCATION')
#Decoding a QRCode
#Saved Location is the name of file with extension of the qr code
decoded=decode(Image.open('SAVED LOCATION'))
#This print statement will print the data you have added
print(str(decoded[0].data)[2:-1])

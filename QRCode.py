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
decoded=decode(Image.open('SAVED LOCATION'))
print(str(decoded[0].data)[2:-1])

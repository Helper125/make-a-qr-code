import qrcode #you need to download the library(pip install qrcode(it is to make a qr-code), pip install Pillow(it's to make an image))

inp = input("enter what you want to insert into the qr-code")
save = input("enter the name of the qr-code file")
picture = qrcode.make(inp)
picture.save(save +'.png')
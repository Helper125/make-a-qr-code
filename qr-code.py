import qrcode

inp = input("enter what you want to insert into the qr-code")
save = input("enter the name of the qr-code file")
picture = qrcode.make(inp)
picture.save(save +'.png')
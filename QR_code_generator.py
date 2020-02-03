# importing the QR code module
import qrcode
# defining the arguments required for generating the QR_code.
code = qrcode.QRCode(version=1, box_size=10, border = 5)
# assigning the message required to be store in the variable.
content = "Hi, this QR code can be certainly play a vital role wherever Unique Identification Feature is required."
# store the message into the generated QR_code 
code.add_data(content)
code.make(fit = True)
# assigning the generated QR_code into the variable.
pic=code.make_image(fill = "black", back_colour = "white")
# save the generated QR_code as a pic.
pic.save("QR_code_message.png")
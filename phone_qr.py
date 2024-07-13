#IMPORTANT 
#Read these comments 

#Don't feel like spelling out your number to someone?
#Maybe for security resons or something.
#make a qr code for your phone number.
#simple stuff let's break it down, not dancing.

#prerequisite - download qrcode using pip command == pip install qrcode
#prerequisite 2 - import the different stuff you need (google is your friend) 

#modules are the parts of the qr that are scanned usually black and the background is white, eyes are the corners of the qr always watching

# step 1 make a variable for your phone number "tel:" to show that its a phone number (will open the phone app)
# step 2 make the qr code image (no data yet) version (size/number/complexity of the modules) error_correction(helps to keep the qr readable) 
#            box_zize(obvious the size of the thing) border(space outside the qr itself)
#step 3 add the data(the phone number)
#step 4 (optional) fit the image 
#you can stop after step 4 for a basic qr but if you want to customize abit lets go step 5 

#step 5 - make the qr how you want but for this its circular and rounded.
#             image_factory(so you can add different colors and shapes) module_drawer(change the shape of the modules for now that is Circles)
#             eye_drawer(like module drawer its to change the shape and here rounded was used) 
 
# you can end here but next part is for custom colors

#             color mask only accpets RGB  so time to mix until you're satisfied 
#             ( change the color of the modules and background back_color is for background and front is for modules)





import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from qrcode.image.styles.colormasks import RadialGradiantColorMask

phone_number = "tel: "

# Create a QR code
qr = qrcode.QRCode(
    version=5,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=70,
    border=2
)
qr.add_data(phone_number)
qr.make(fit=True)

# Create an image from the QR code with circular modules and rounded eyes
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),  # Use CircleModuleDrawer for circular modules
    eye_drawer=RoundedModuleDrawer(),    # Use RoundedModuleDrawer for rounded eyes
    color_mask=SolidFillColorMask(
        back_color=(11, 11, 11), 
        front_color=(255, 255, 255),
        eye_color=(255,0,0)
    )
)

# Save the image
img.save("phone_qr.png")

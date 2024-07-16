#this is an update to phone_qy.py 
#fixed issues regarding the eyes and allowed different colors using masks
#explainations provided by chatGpt(im too tired today man) and are included in the code where needed
#have fun it was my blood sweat and tears

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, RoundedModuleDrawer
from qrcode.image.styles.colormasks import SolidFillColorMask
from PIL import Image, ImageDraw

# Step 1: Define the phone number with "tel:" prefix
phone_number = "tel: "

# Step 2: Create a QRCode object with specified settings
qr = qrcode.QRCode(
    version=5,  # QR code version (size/number of modules)
    error_correction=qrcode.constants.ERROR_CORRECT_L,  # Error correction level
    box_size=10,  # Size of each module
    border=4  # Thickness of the border
)

# Step 3: Add the phone number data to the QR code
qr.add_data(phone_number)
qr.make(fit=True)  # Fit the QR code to the optimal size

# Step 4: Create the QR code image with rounded eyes
eye_img = qr.make_image(
    image_factory=StyledPilImage,
    eye_drawer=RoundedModuleDrawer(),  # Use RoundedModuleDrawer for rounded eyes
    color_mask=SolidFillColorMask(
        back_color=(1, 1, 1),  # Background color (white)
        front_color=(255,255, 255)  # Eye color (custom color)
    )
)

# Step 5: Create the main QR code image with Cicular-shaped modules
img = qr.make_image(
    image_factory=StyledPilImage,
    module_drawer=CircleModuleDrawer(),  # Use CircleModuleDrawer for Circle-shaped modules
    color_mask=SolidFillColorMask(
        back_color=(1, 1, 1),  # Background color (white)
        front_color=(220, 00, 255)  # Module color (custom color)
    )
)

# Step 6: Define a function to style the eyes with a mask
def style_eyes(img):
    img_size = img.size[0]
    eye_size = 79  # Increased eye size
    quiet_zone = 40  # Default quiet zone (border)
    
    # Create a mask image
    mask = Image.new('L', img.size, 0)
    draw = ImageDraw.Draw(mask)
    
    # Define the eye positions (adjust as needed)
    eye_positions = [
        (quiet_zone, quiet_zone, quiet_zone + eye_size, quiet_zone + eye_size),
        (img_size - eye_size - quiet_zone, quiet_zone, img_size - quiet_zone, quiet_zone + eye_size),
        (quiet_zone, img_size - eye_size - quiet_zone, quiet_zone + eye_size, img_size - quiet_zone)
    ]
    
    # Draw rectangles for the eyes on the mask
    for (x1, y1, x2, y2) in eye_positions:
        draw.rectangle([x1, y1, x2, y2], fill=255)
    
    return mask

# Step 7: Apply the mask to composite the eye image onto the main QR code image
mask = style_eyes(img)
final_img = Image.composite(eye_img, img, mask)

# Step 8: Save the final QR code image
final_img.save("fixed.png")

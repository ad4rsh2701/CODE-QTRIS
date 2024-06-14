import qrcode
from PIL import Image, ImageDraw

def generate_qr_code(data, file_path="assets/qr_code.png"):
    # Generate QR code image
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white")


    # Convert QR code image to RGBA to allow for transparency
    qr_img = qr_img.convert('RGBA')

    # Define outline color (gray)
    outline_color = (169, 169, 169, 255)

    # Create a blank image for drawing outlines
    outline_img = Image.new('RGBA', qr_img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(outline_img)

    # Function to check if a pixel is on the edge of a QR code block
    def is_edge_pixel(i, j):
        if qr_img.getpixel((i, j)) == (0, 0, 0, 255):  # If pixel is black (QR code block)
            # Check adjacent pixels horizontally and vertically
            if (i == 0 or qr_img.getpixel((i-1, j)) == (255, 255, 255, 255)) or \
               (i == qr_img.size[0]-1 or qr_img.getpixel((i+1, j)) == (255, 255, 255, 255)) or \
               (j == 0 or qr_img.getpixel((i, j-1)) == (255, 255, 255, 255)) or \
               (j == qr_img.size[1]-1 or qr_img.getpixel((i, j+1)) == (255, 255, 255, 255)):
                return True
        return False

    # Draw outlines on the blank image
    for i in range(qr_img.size[0]):
        for j in range(qr_img.size[1]):
            if is_edge_pixel(i, j):
                draw.point((i, j), outline_color)

    # Composite the QR code image with outlines
    final_img = Image.alpha_composite(qr_img, outline_img)

    # Change white pixels to black
    pixels = final_img.load()
    for i in range(final_img.size[0]):
        for j in range(final_img.size[1]):
            if pixels[i, j] == (255, 255, 255, 255):  # If pixel is white
                pixels[i, j] = (0, 0, 0, 255)  # Change it to black

    # Save the final image
    final_img.save(file_path)

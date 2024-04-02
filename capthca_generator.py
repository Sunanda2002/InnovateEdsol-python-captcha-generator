from PIL import Image, ImageDraw, ImageFont
import random
import string

# Function to generate a random string for CAPTCHA
def generate_captcha():
    characters = string.ascii_letters + string.digits
    captcha_text = ''.join(random.choice(characters) for _ in range(6))  # Generate a 6-character string
    return captcha_text

# Function to generate a CAPTCHA image
def generate_captcha_image(text, filename):
    width, height = 200, 100  # Image dimensions
    background_color = (255, 255, 255)  # White background
    text_color = (0, 0, 0)  # Black text color


    # Create a new image with white background
    image = Image.new('RGB', (width, height), color=background_color)
    font = ImageFont.truetype('timesi.ttf', size=50)
    # Create a drawing object
    draw = ImageDraw.Draw(image)

    # Draw text on the image
    draw.text((10, 40), text, fill=text_color,font=font)

    # Save the image to a file
    image.save("capt.png")

if __name__ == "__main__":
    captcha_text = generate_captcha()
    generate_captcha_image(captcha_text, "capt.png")
    print("CAPTCHA image has been generated as 'capt.png'.")

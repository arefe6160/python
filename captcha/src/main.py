import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

WIDTH = 300
HEIGHT = 100
FONT_SIZE = 60
CAPTCHA_LENGTH = 5

def generate_random_text(length=5):
    chars = string.ascii_uppercase
    return ''.join(random.choice(chars) for _ in range(length))

def generate_random_color():
    return (
        random.randint(0, 200),
        random.randint(0, 200),
        random.randint(0, 200)
    )

def add_noise(draw, width, height):
    for _ in range(1000):
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.point((x, y), fill=generate_random_color())

def draw_random_line(draw, width, height):
    draw.line(
        (
            0, random.randint(0, height//2),
            width, random.randint(0, height//2)
        ),
        fill=generate_random_color(),
        width=5
    )

def generate_captcha_image():
    image = Image.new("RGB", (WIDTH, HEIGHT), (255, 255, 255))
    draw = ImageDraw.Draw(image)

    text = generate_random_text(CAPTCHA_LENGTH)

    try:
        font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    except IOError:
        font = ImageFont.load_default()

    x_offset = 20

    for char in text:
        char_image = Image.new("RGBA", (80, 80), (255, 255, 255, 0))
        char_draw = ImageDraw.Draw(char_image)

        char_draw.text((10, 5), char, font=font, fill=generate_random_color())

        rotated_char_image = char_image.rotate(random.randint(-30, 30), expand=1)

        image.paste(rotated_char_image, (x_offset, random.randint(10, 30)), rotated_char_image)
        x_offset += 50

    add_noise(draw, WIDTH, HEIGHT)
    draw_random_line(draw, WIDTH, HEIGHT)
    image = image.filter(ImageFilter.SMOOTH)

    output_filename = "captcha.png"
    image.save(output_filename)
    print(f"Generated CAPTCHA image saved as: {output_filename}")
    print(f"The CAPTCHA text was: {text}")

if __name__ == "__main__":
    generate_captcha_image()

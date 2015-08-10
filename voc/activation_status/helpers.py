__author__ = 'khatcher'

import StringIO
from PIL import Image, ImageDraw, ImageFont

from flask import send_file


def serve_pil_image(pil_img):
    img_io = StringIO.StringIO()
    pil_img.save(img_io, 'JPEG', quality=70)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')


def make_image(message, path, width=5000, height=1250, txtsize=1200):
    red = (255,0,0)
    yellow = (255,255,0)
    green = (0,255,0)
    if message == "montoring":
        bg_color = green
    elif message == "partial":
        bg_color = yellow
    elif message == "full":
        bg_color = red
    image = Image.new("RGBA", (width,height), bg_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("Arial.ttf", txtsize)
    msgw, msgh = font.getsize(message)
    print msgw, msgh
    msgt = ((height/2)-(msgh/2))
    msgl = ((width/2)-(msgw/2))
    print msgt, msgl
    draw.fontmode = "1"
    draw.text( (msgl,msgt), message, (0,0,0), font=font)
    draw.text( (msgl,msgt), message, (0,0,0), font=font)
    image_resized = image.resize((500,125), Image.ANTIALIAS)
    return image_resized
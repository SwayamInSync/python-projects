from PIL import Image, ImageDraw, ImageFont


# creating image object from image

def watermark(image, mark):
    im = Image.open(image)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = str(mark)

    font = ImageFont.truetype("Times New Roman", 40)
    textwidth, textheight = draw.textsize(text=text, font=font)

    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    draw.text((x, y), text=text, font=font)
    im.show()

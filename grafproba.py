from PIL import Image, ImageDraw
import random

width = 2000
height = 1600
im = Image.new('L', (width, height))
# palette = []
# for i in range(0, 255):
#     j = i % 8
#     k = (i // 8) % 8
#     l = i // 64
#     palette.append(j)
#     palette.append(k)
#     palette.append(l)
# im.putpalette(palette, 'RGB')
color = 1

draw = ImageDraw.Draw(im)

for color in range(0, 255):
    a = random.randint(0, width)
    b = random.randint(0, height)
    c = random.randint(0, width)
    d = random.randint(0, height)
    draw.line((a, b, c, d), fill=color, width=40, joint="curved")

for i in range(0, 100):
    for j in range(0, 100):
        im.putpixel((i, j), color)
del draw
im.show()
im.save("rudak1.jpg")

from PIL import Image, ImageDraw, ImageFont
from PIL import BdfFontFile as font
import numpy as np
import random

WIDTH = 2000
HEIGHT = 1600
AREA = WIDTH * HEIGHT
MARGIN = 7
DENSITY = 0.95
FILLCOLOR = 0 # 0...255

random.seed()

im1 = Image.new('L', (WIDTH, HEIGHT))
draw1 = ImageDraw.Draw(im1)
im2 = Image.new('L', (WIDTH, HEIGHT))
draw2 = ImageDraw.Draw(im2)

s = 0.0
drop_list = []

def min_distance(x, y):
    md = min(x, WIDTH - x, y, HEIGHT - y)
    if len(drop_list) > 0:
        for (u, v, r) in drop_list:
            d = np.sqrt((x - u) * (x - u) + (y - v) * (y - v))
            if d - r - MARGIN < md:
                md = d - r - MARGIN
    return md

while s < DENSITY * AREA:
    radius = -1
    while (radius < MARGIN):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = min_distance(x, y)
    if radius >= MARGIN:
        drop_list.append((x, y, radius))
        draw1.ellipse((x - radius, y - radius, x + radius, y + radius), fill= FILLCOLOR, outline=255, width=3)
        s += (radius + MARGIN) * (radius + MARGIN) * np.pi
    else:
        print(x, y, radius)

print(s / AREA)
im1.show()
im1.save("droplets.jpg")

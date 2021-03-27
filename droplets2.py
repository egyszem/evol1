from PIL import Image, ImageDraw, ImageFont
from PIL import BdfFontFile as font
import numpy as np
import random
from dataclasses import dataclass

WIDTH = 2000
HEIGHT = 1600
AREA = WIDTH * HEIGHT
DENSITY = 0.95

seed = 13

random.seed(seed)

im = Image.new('L', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)

s = 0.0
disk_list = []

def spread(a, b, c, d):
    return np.sqrt((a - c) * (a - c) + (b - d) * (b - d))
k = 2000

while k > 0:
    k -= 1
    print(k)
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    draw.ellipse((x - 2, y - 2, x + 2, y + 2), fill= 0, outline=255, width=1)
    radius = min(x, WIDTH - x, y, HEIGHT - y)
    depth  = 0

    if len(disk_list) > 0:
         for (u, v, r, d) in disk_list:
            distance = spread(u, v, x, y) - r
            if distance < 0:
                radius = - distance
                if d >= depth:
                    depth = d + 1
            else:
                if distance < radius:
                    radius = distance
    radius -= 4
    if radius > 0:
        disk_list.append((x, y, radius, depth))
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=255 * (1 - depth % 2), outline=255, width=3)
im.show()
im.save("NEWdroplets.jpg")

from PIL import Image, ImageDraw, ImageFont
from PIL import BdfFontFile as font
import numpy as np
import random

version = 1

random.seed()
im = Image.new('L', (1800, 1600))
draw = ImageDraw.Draw(im)
font = ImageFont.truetype("arial.ttf", 45)

WIDTH = 1800
HEIGHT = 1600
CONTRACTION = 0.94  # parameter 1: contraction rate
ANGLE4_DIFF = 0.008 * np.pi
ANGLE3_DIFF = 0.008 * np.pi
ANGLE2_DIFF =  0.05 * np.pi
ANGLE1_DIFF = 0.5 * np.pi
START_LENGTH = 100.0  # parameter 3: initial branch length
MIN_LENGTH = 4

for i in range(0, 5):
    x = 0
    y = (2 * i + 1) / 10 * HEIGHT
    if i < 2:
        draw.text((WIDTH - 600, y), '1-order random line', fill=255, font=font)
    if i == 2:
        draw.text((WIDTH - 600, y), '0-order random line', fill=255, font=font)
    if i > 2:
        draw.text((WIDTH - 600, y), '2-order random line', fill=255, font=font)
    if i == 1 or i == 4:
        draw.text((WIDTH - 600, y + 45), 'with upward bending', fill=255, font=font)
    angle = 0
    angle2 = 0
    length = START_LENGTH
    while (length > MIN_LENGTH):
        u = int(x + np.cos(angle) * length)
        v = int(y - np.sin(angle) * length)
        draw.line(((x, y, u, v)), fill=255, width=4, joint="None")
        if i == 0:
            angle += random.uniform(-1, 1) * ANGLE2_DIFF
        if i == 1:
            angle += np.sign(np.pi / 2 - angle) * random.uniform(0, 1) * ANGLE2_DIFF
        if i == 2:
            angle = random.uniform(-1, 1) * ANGLE1_DIFF
        if i == 3:
            angle2 += random.uniform(-1, 1) * ANGLE3_DIFF
            angle += angle2
        if i == 4:
            angle2 += np.sign(np.pi / 2 - angle) * random.uniform(0, 1) * ANGLE4_DIFF
            angle += angle2
        length = CONTRACTION * length
        x = u
        y = v
im.show()
im.save("randcurve1{version}.jpg")

from PIL import Image, ImageDraw
import numpy as np
import random

random.seed()
im = Image.new('L', (1800, 1600))

draw = ImageDraw.Draw(im)

WIDTH = 1800
HEIGHT = 1600
CONTRACTION = 0.94  # parameter 1: contraction rate
ANGLE3_DIFF = 0.005 * np.pi
ANGLE2_DIFF =  0.05 * np.pi
ANGLE1_DIFF = 0.5 * np.pi
START_LENGTH = 100.0  # parameter 3: initial branch length
MIN_LENGTH = 4

print(np.log(START_LENGTH / MIN_LENGTH) / np.log(2))
# 1. vonal
x = 0
y = 1 / 8 * HEIGHT
angle = 0
length = START_LENGTH
while (length > MIN_LENGTH):
    u = int(x + np.cos(angle) * length)
    v = int(y - np.sin(angle) * length)
    draw.line(((x, y, u, v)), fill=255, width=4, joint="None")
    angle = random.uniform(-1, 1) * ANGLE1_DIFF
    length = CONTRACTION * length
    x = u
    y = v
# 2. vonal
x = 0
y = 3 / 8 * HEIGHT
angle = 0
length = START_LENGTH
while (length > MIN_LENGTH):
    u = int(x + np.cos(angle) * length)
    v = int(y - np.sin(angle) * length)
    draw.line(((x, y, u, v)), fill=255, width=4, joint="None")
    angle += random.uniform(-1, 1) * ANGLE2_DIFF
    length = CONTRACTION * length
    x = u
    y = v
#3. vonal
x = 0
y = 5 / 8 * HEIGHT
angle = 0
angle2 = 0
length = START_LENGTH
while (length > MIN_LENGTH):
    u = int(x + np.cos(angle) * length)
    v = int(y - np.sin(angle) * length)
    draw.line(((x, y, u, v)), fill=255, width=4, joint="None")
    angle2 += random.uniform(-1, 1) * ANGLE3_DIFF
    angle += angle2
    length = CONTRACTION * length
    x = u
    y = v
#4. vonal
x = 0
y = 7 / 8 * HEIGHT
angle = 0
angle2 = 0
length = START_LENGTH
while (length > MIN_LENGTH):
    u = int(x + np.cos(angle) * length)
    v = int(y - np.sin(angle) * length)
    draw.line(((x, y, u, v)), fill=255, width=4, joint="None")
    angle2 += np.sign(np.pi / 2 - angle) * random.uniform(0, 1) * ANGLE3_DIFF
    angle += angle2
    length = CONTRACTION * length
    x = u
    y = v
im.show()
im.save("randcurve1.jpg")

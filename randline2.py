# the images were made by this  -- this time using recursive function calls

from PIL import Image, ImageDraw
import numpy as np
import random
import utils

#val = input("random seed: ")
val = 777
random.seed(val)
WIDTH = 1800
HEIGHT = 1600
MIN_STEP = 2.81
RAY = 80
N = 50
GENERATION = 10

im = Image.new('L', (WIDTH, HEIGHT))

draw = ImageDraw.Draw(im)

def lines(a):
    x, y = WIDTH / 2, HEIGHT / 2
    u, v = RAY * np.cos(a), RAY * np.sin(a)
    delta_u, delta_v = 0, 0
    i = GENERATION
    while (i > 0):
        i -= 1
        draw.line((int(x), int(y), int(x + u), int(y + v)), fill=255, width=4, joint="curved")
        x = (x + u) % WIDTH
        y = (y + v) % HEIGHT
        u += delta_u
        v += delta_v
        delta_u += random.uniform(-1, 1) * MIN_STEP
        delta_v += random.uniform(-1, 1) * MIN_STEP

for k in range(0, N):
    random.seed(val)
    lines(2 * k * np.pi / N)

im.show()
#file_path = f"randfa/images/randline2_{val}.jpg"
#im.save(file_path)

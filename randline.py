# the images were made by this  -- this time using recursive function calls

from PIL import Image, ImageDraw
import numpy as np
import random
import utils

val = input("random seed: ")
random.seed(val)
WIDTH = 1800
HEIGHT = 1600

im = Image.new('L', (WIDTH, HEIGHT))

draw = ImageDraw.Draw(im)

CONTRACTION = 0.88
START_X = WIDTH // 2
START_Y = HEIGHT - 1
START_LENGTH = 5.0
START_ANGLE = 0.5 * np.pi
MIN_LENGTH = 6.0
CURVATURE_MAX = 0.00005 * np.pi


def line(x, y, length, angle):  # drawing a subtree
    angle2 = 0.0

    while (length > MIN_LENGTH):
        u = x + length * np.cos(angle)
        v = y - length * np.sin(angle)
        length = CONTRACTION * length
        curvature = random.uniform(-1, 1) * CURVATURE_MAX * length * length
        angle2 += curvature
        angle += angle2
        line_width = int(0.4 * length)
        draw.line(((int(x), int(y), int(u), int(v))), fill=255, width=line_width, joint="curved")
        x = u
        y = v


def lines(x, y, length, angle):  # drawing a subtree
    angle2 = 0.0

    i = 10000
    while (i > 0):
        i -= 1
        u = x + length * np.cos(angle)
        v = y - length * np.sin(angle)
        curvature = random.uniform(-1, 1) * CURVATURE_MAX
        angle2 += curvature
        angle += angle2
        line_width = 2
        draw.line(((int(x), int(y), int(u), int(v))), fill=255, width=line_width, joint="curved")
        x = u % WIDTH
        y = v % HEIGHT


lines(START_X, START_Y, START_LENGTH, START_ANGLE)
im.show()
file_path = f"randfa/images/randline_{val}.jpg"
im.save(file_path)

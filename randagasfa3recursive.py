# the images were made by this  -- this time using recursive function calls

from PIL import Image, ImageDraw
import numpy as np
import random
import utils

random.seed()
im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
WIDTH = 1800
HEIGHT = 1600
CONTRACTION = 0.88  # parameter 1: lower bound for contraction
CONTRACTION_STEP = 0.06  # parameter 2: step for contraction
START_X = WIDTH // 2
START_Y = HEIGHT - 1
START_LENGTH = 80.0  # parameter 3: 1. starting section length
START_ANGLE = 0.5 * np.pi
MIN_LENGTH = 6.0  # parameter 4: smallest section length: with 2.0 it looks fuzzy, with 10.0 clean
CURVATURE_MAX = 0.002 * np.pi  # parameter 5: curvature max = 0.035 pi = 6.3 degrees
BRANCH_ANGLE = 0.25 * np.pi  # parameter 6: max branching angle
BRANCHING_PROBABILITY = 0.2  # parameter 7: probability of branching


def branch(x, y, length, angle):  # drawing a subtree
    angle2 = 0.0

    while (length > MIN_LENGTH):
        u = int(x + length * np.cos(angle))
        v = int(y - length * np.sin(angle))
        length = (CONTRACTION + random.choice((0, 1, 2)) * CONTRACTION_STEP) * length
        curvature = np.sign(START_ANGLE - angle) * random.uniform(0, 1) * CURVATURE_MAX
        angle2 += curvature
        angle += angle2
        line_width = int(0.4 * length)
        draw.line(((x, y, u, v)), fill=255, width=line_width, joint="curved")
        x = u
        y = v
        if random.random() < BRANCHING_PROBABILITY:
            new_angle = angle + random.uniform(-1, 1) * BRANCH_ANGLE
            branch(x, y, length, new_angle)


branch(START_X, START_Y, START_LENGTH, START_ANGLE)
im.show()
file_path = f"randfa/images/randagasfa3recursive_{utils.get_date_string()}.jpg"
im.save(file_path)

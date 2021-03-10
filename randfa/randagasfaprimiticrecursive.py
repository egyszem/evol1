from PIL import Image, ImageDraw
import numpy as np
import random

random.seed()
im = Image.new('L', (1800, 1600))

draw = ImageDraw.Draw(im)

WIDTH = 1800
HEIGHT = 1600
CONTRACTION = 0.7  # parameter 1: contraction rate
ANGLE_TURN = 0.16 * np.pi  # parameter 2: fix angle turn for new branches
START_X = WIDTH // 2
START_Y = HEIGHT - 1
START_LENGTH = 1000.0  # parameter 3: initial branch length
START_ANGLE = 0.5 * np.pi
BRANCH_NUMBER = 2
MIN_BRANCH_LENGTH = 125


def branch(x, y, length, angle, angle_turn):
    u = int(x + np.cos(angle) * length)
    v = int(y - np.sin(angle) * length)
    draw.line(((x, y, u, v)), fill=255, width=10, joint="None")
    angle_turn = random.choice((-angle_turn, angle_turn))
    length = CONTRACTION * length
    r = 0
    if length > MIN_BRANCH_LENGTH:
        for i in range(0, BRANCH_NUMBER):
            r = random.uniform(r, length)
            angle_turn = -angle_turn
            u = int(x + np.cos(angle) * r)
            v = int(y - np.sin(angle) * r)
            branch(u, v, length, angle + angle_turn, angle_turn)


branch(START_X, START_Y, START_LENGTH, START_ANGLE, random.choice((ANGLE_TURN, -ANGLE_TURN)))  # ag megrajzolasa
im.show()
im.save("randagasfaprimitiv5.jpg")

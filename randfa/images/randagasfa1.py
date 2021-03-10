# ez a jó, ezzel csináltam a rajzokat

from PIL import Image, ImageDraw
import numpy as np
import random

im = Image.new('L', (1800, 1600))
random.seed()
draw = ImageDraw.Draw(im)

WIDTH = 1800
HEIGHT = 1600
CONTRACTION = 0.88  # 1. paraméter: szakaszrövidülési kvóciens alsó határa, 0, 1 vagy 2 CONTRACTION_STEP-pel nőhet
CONTRACTION_STEP = 0.06
START_X = WIDTH // 2
START_Y = HEIGHT - 1
START_LENGTH = 80.0  # 2. paraméter: 1. szakasz hossza
START_ANGLE = 0.5 * np.pi
MIN_LENGTH = 3.0  # 3. paraméter: legkisebb szakaszhossz -- 2.0-nél bolyhos a vége, 10.0-nál már nem
MIN_CURVATURE = 0.01 * np.pi  # = 3 fok        # 5. paraméter: görbület, itt 0.01 Pi = 3 fok
MAX_BRANCHING_ANGLE = 0.25 * np.pi  # 45 fok             # 7. paraméter: elágazási szög, -Pi/4 ... Pi/4
BRANCHING_PROBABILTY = 0.27  # 6. paraméter: elágazási valószínűség: itt 20%

branchlist = [(START_X, START_Y, START_LENGTH, START_ANGLE)]


def branch(x, y, length, angle):
    branchlist.remove((x, y, length, angle))
    angle2 = 0.0

    while (length > MIN_LENGTH):
        u = int(x + length * np.cos(angle))
        v = int(y - length * np.sin(angle))
        length = int((CONTRACTION + CONTRACTION_STEP * random.randint(0, 2)) * length)
        curvature = random.uniform(-1, 1) * MIN_CURVATURE
        angle2 += curvature
        angle += angle2
        draw.line(((x, y, u, v)), fill=255, width=int(0.4 * length), joint="curved")
        x = u
        y = v
        if (random.random() < BRANCHING_PROBABILTY):
            branchlist.append((x, y, length, angle + random.uniform(-1, 1) * MAX_BRANCHING_ANGLE))


while len(branchlist) > 0:
    r = random.randint(0, len(branchlist) - 1)
    (START_X, START_Y, START_LENGTH, START_ANGLE) = branchlist[r]
    branch(START_X, START_Y, START_LENGTH, START_ANGLE)
print(len(branchlist))
im.show()
im.save("randagasfa121.jpg")

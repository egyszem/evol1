# ez a jó, ezzel csináltam a rajzokat -- csak most rekurzív függvényhívással

from PIL import Image, ImageDraw
import numpy as np
import random
import utils

val = input("random seed ")
random.seed(val)

im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
# TODO: csupa nagybetűvel a globális változókat - konstansokat
WIDTH = 1800
HEIGHT = 1600

START_X = WIDTH // 2
START_Y = HEIGHT - 1
START_LENGTH = 100  # 1. paraméter: első szakasz hossza
START_ANGLE = 0.5 * np.pi
MIN_LENGTH = 6.0  # 2. paraméter: legkisebb szakaszhossz -  2.0-nél nagyon bolyhos a vége, 10.0-nál már nem
LENGTH_LOG = np.log(START_LENGTH / MIN_LENGTH)
CONTRACTION = 0.88  # 3-4. paraméter: szakaszrövidülési kvóciens alsó határa és differencija
DELTA_CONTRACTION = 0.06
CURVATURE_STEP = 0.25 * np.pi  # 5. paraméter: a szögváltozás változása,  nagyon érzékeny a konkrét paraméterekre
BRANCHING_PROBABLITY = 0.18
BRANCHING_ANGLE = 0.45 * np.pi  # parameter 6: max branching angle


def branch(x, y, length, angle):  # ágrajzolás
    # angle: másodfokban változik random
    angle2 = 0.0
    while length > MIN_LENGTH:
        u = int(x + length * np.cos(angle))
        v = int(y - length * np.sin(angle))
        length = int((CONTRACTION + random.randint(0, 2) * DELTA_CONTRACTION) * length)
        curvature = random.uniform(-0.5, 0.5) * CURVATURE_STEP
        #angle2 += curvature
        angle2 = curvature
        angle += angle2
        draw.line((x, y, u, v), fill=255, width=int(0.4 * length), joint="curved")
        x = u
        y = v
        branching_angle = random.uniform(-1, 1) * BRANCHING_ANGLE
        if random.random() < BRANCHING_PROBABLITY:
            branch(x, y, length, angle + branching_angle)

branch(START_X, START_Y, START_LENGTH, START_ANGLE)
im.show()
file_path = f"randfa/images/randagasfa3_{utils.get_date_string()}.jpg"
im.save(file_path)
print(LENGTH_LOG, np.pi)

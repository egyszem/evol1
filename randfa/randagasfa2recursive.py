# ez a jó, ezzel csináltam a rajzokat -- csak most rekurzív függvényhívással

from PIL import Image, ImageDraw
import numpy as np
import random

import utils

random.seed()

im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
# TODO: csupa nagybetűvel a globális változókat - konstansokat
WIDTH = 1800
height = 1600
contraction = 0.88  # 1. paraméter: szakaszrövidülési kvóciens alsó határa

start_x = WIDTH // 2
start_y = height - 1
start_length = 80  # 2. paraméter: 1. szakasz hossza
start_angle = 0.5 * np.pi

MIN_LENGTH = 4.0

def branch(x, y, length, angle):  # ágrajzolás
    # angle: másodfokban változik random

    while length > MIN_LENGTH:
        # egymás után fűzött szakaszok # 2.0-nél nagyon bolyhos a vége, 10.0-nál már nem
        # 3. paraméter: legkisebb szakaszhossz
        u = int(x + length * np.cos(angle))
        v = int(y - length * np.sin(angle))
        # 4. paraméter: szakaszrövidülési kvóciens intervalluma: itt contraction = 0.88...0.94
        length = int((contraction + 0.06 * random.randint(0, 2)) * length)
        curvature = 0.0001 * (random.randint(0, 1000) - 501) * np.pi
        # kvázi görbület: a szögváltozás változása,  nagyon érzékeny a konkrét paraméterekre / = 0.0175 Pi = 3.15 fok
        # 5. paraméter: szakaszgörbület, itt 0.0175 Pi
        angle += curvature
        draw.line((x, y, u, v), fill=255, width=int(0.4 * length), joint="curved")
        x = u
        y = v

        if (random.randint(0, 100) < 27) and (random.randint(0, 45) > np.log(length)):
            # 6. paraméter: elágazási valószínűség: itt 27% and (0.9... 1,0)) -- különös feltétel
            # 7. paraméter: elágazási szög, itt - Pi/4 ... Pi/4
            branch(x, y, length, angle + .025 * (random.randint(0, 20) - 10) * np.pi)


branch(start_x, start_y, start_length, start_angle)
im.show()
file_path = f"images/randagasfa2_{utils.get_date_string()}.jpg"
im.save(file_path)

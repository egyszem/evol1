from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

seed = input("random seed: ")
random.seed(seed)

WIDTH = 23
HEIGHT = 15

WALL = 40

im = Image.new('L',(2 * WIDTH * WALL, 2 * HEIGHT * WALL))
draw = ImageDraw.Draw(im)


def block(x1, y1, x2, y2, k):
    if (x2 - x1 >= 2) and (y2 - y1 >=2) and (k > 0):
        u = 2 * x1 * WALL
        v = 2 * y1 * WALL
        w = 2 * x2 * WALL
        z = 2 * y2 * WALL
        case = random.randint(0, 3)
        print("case: ", case)
        if case % 2 == 1:
            print("függ")
            a = random.randint(x1 + 1, x2 - 1)
            c = a + 1
            print(x1, y1, x2, y2, "->", x1, y1, a, y2)
            print(x1, y1, x2, y2, "->", c, y1, x2, y2)
            u = 2 * a * WALL
            w = (2 * a + 1) * WALL
            if case == 1:
                z -= WALL
            elif case == 3:
                v += WALL
            s = input("")
            draw.rectangle((u, v, w, z), fill=255, width=1)
            im.show()
            block(x1, y1, a, y2, k - 1)
            block(c, y1, x2, y2, k - 1)
        else:
            print("vízsz")
            b = random.randint(y1 + 1, y2 - 1)
            d = b + 1
            print(x1, y1, x2, y2, "->", x1, y1, x2, b)
            print(x1, y1, x2, y2, "->", x1, d, x2, y2)
            v = 2 * b * WALL
            z = (2 * b + 1) * WALL
            if case == 0:
                w -= WALL
            elif case == 2:
                u += WALL
            s = input("")
            draw.rectangle((u, v, w, z), fill=255, width=1)
            im.show()
            block(x1, y1, x2, b, k  - 1)
            block(x1, d, x2, y2, k - 1)


block(0, 0, WIDTH,HEIGHT, 5)
im.show()
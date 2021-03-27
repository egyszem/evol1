from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

seed = input("random seed: ")
random.seed(seed)

WIDTH = 32
HEIGHT = 24

WALL = 40
im = Image.new('L', ((2 * WIDTH - 1) * WALL, (2 * HEIGHT - 1) * WALL))
draw = ImageDraw.Draw(im)


def draw_block(u, v, w, z):
    draw.rectangle(((u - 1) * WALL, (v - 1) * WALL, (w - 1) * WALL, (z - 1) * WALL), fill=192, width=1)


def block(x1, y1, x2, y2):
    w = x2 - x1
    h = y2 - y1
    if w >= 4 and h >= 4:
        if random.randint(0, w + h) < w:
            a = random.randrange(x1 + 2, x2, 2)
            if random.choice((0, 1)) == 0:
                draw_block(a, y1 + 2, a + 1, y2)
            else:
                draw_block(a, y1, a + 1, y2 - 1)
            block(x1, y1, a, y2)
            block(a, y1, x2, y2)
        else:
            b = random.randrange(y1 + 2, y2, 2)
            if random.choice((0, 1)) == 0:
                draw_block(x1, b, x2 - 1, b + 1)
            else:
                draw_block(x1 + 2, b, x2, b + 1)
            block(x1, y1, x2, b)
            block(x1, b, x2, y2)


def Block(w, h, with_frame=True):
    if not with_frame:
        block(0, 0, w, h)
        return
    r = random.randrange(2, h-2, 2)
    draw_block(1, 1, 2, r)
    draw_block(1, r + 1, 2, h)
    r = random.randrange(2, h-2, 2)
    draw_block(w - 1, 1, w, r)
    draw_block(w - 1, r + 1, w, h)
    r = random.randrange(2, w - 2, 2)
    draw_block(1, 1, r, 2)
    draw_block(r + 1, 1, w, 2)
    r = random.randrange(2, w - 2, 2)
    draw_block(1, h - 1, r, h)
    draw_block(r + 1, h - 1, w, h)
    block(1, 1, w - 1, h - 1)


Block(2 * WIDTH, 2 * HEIGHT, with_frame=True)
im.show()

im.save("images\maze_divide" + str(seed) + ".jpg")
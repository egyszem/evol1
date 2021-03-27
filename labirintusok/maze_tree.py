from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

random.seed()

WIDTH = 32
HEIGHT = 24

WALL = 40
im = Image.new('L', ((2 * WIDTH - 1) * WALL, (2 * HEIGHT - 1) * WALL))
draw = ImageDraw.Draw(im)

def draw_block(u, v, w, z):
    draw.rectangle((u * WALL, v * WALL, w * WALL, z * WALL), fill=192, width=1)

def draw_square(u, v):
    draw.rectangle((u * WALL, v * WALL, (u + 1) * WALL,(v + 1) * WALL), fill=192, width=1)

def is_free_square(u, v):
    return im.getpixel((u * WALL, v * WALL)) == 0

def occupy_square(u, v):
    im.putpixel((u * WALL, v * WALL), 255)

def block(x, y):
    draw_square(x, y)
    z = []
    for (u, v) in ((x - 2, y), (x, y - 2), (x + 2, y), (x, y + 2)):
        if u in range(0, 2 * WIDTH) and v in range(0, 2 * HEIGHT):
            if is_free_square(u, v):
                z.append((u, v))
                occupy_square(u, v)
    while len(z) > 0:
        r = random.randint(0, len(z) - 1)
        u, v = z[r]
        z.remove((u, v))
        draw_square((x + u) // 2, (y + v) // 2)
        block(u, v)

def Block(w, h, with_frame=True):
    if  with_frame:
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
    block(WIDTH // 2, HEIGHT // 2)

#Block(2 * width - 1, 2 * HEIGHT - 1, with_frame=True)
block(WIDTH // 2, HEIGHT // 2)

im.show()

im.save("images\maze_tree.jpg")
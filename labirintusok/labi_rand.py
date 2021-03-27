from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

seed = input("random seed: ")
random.seed(seed)

WIDTH = 32
HEIGHT = 24

WALL = 40
im = Image.new('L', ((2 * WIDTH - 1) * WALL, 2 * (HEIGHT - 1) * WALL))
draw = ImageDraw.Draw(im)

def draw_block(x, y, color):
    draw.rectangle(((x - 1) * WALL, (y - 1) * WALL, x * WALL, y * WALL), fill=color, width=1)

def block():
    for x in range(0, 2 * WIDTH):
        for y in range(0, 2 * HEIGHT):
            if x % 2 == y % 2:
                if x % 2 == 0:
                    draw_block(x, y, 0)
                else:
                    draw_block(x, y, 192)
            elif random.choice((0, 1)) == 0:
                draw_block(x, y, 0)
            else:
                draw_block(x, y, 192)
block()
im.show()
im.save("images\labirintus_rand.jpg")
del draw

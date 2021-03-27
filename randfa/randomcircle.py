# Ranom kör

import random
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw
@dataclass
class Params:
    width: int = 2000
    height: int = 1600
    turn: int = 30
    m: int = 30
    n: int = 4 * m
    kx: int = n // 2
    ky: int = n // 2

im = Image.new('L', (Params.width, Params.height))
draw = ImageDraw.Draw(im)


def drawcircle(params: Params):

    def min_set(a, b):
        return b * (b + 1) // 2

    def max_set(a, b):
        return b * (2 * a - b + 1) // 2

    x = params.width // 2
    y = params.height // 2
    u = random.randint(-params.m, params.m)
    v = random.randint(-params.m, params.m)
    zx = (params.n * u + params.n * (params.n + 1) // 2) // 2
    zy = (params.n * v + params.n * (params.n + 1) // 2) // 2
    kx = params.n // 2
    ky = params.n // 2
    i = params.n

    while i > 0:
        if kx in range(0, i + 1) and zx in range(min_set(i, kx), max_set(i, kx ) + 1):
            cont = []
            if (zx - i) in range(min_set(i - 1, kx - 1), max_set(i - 1, kx - 1) + 1): #i-t kxiválasztjukx
                cont.append(1)
            if zx in range(min_set(i - 1, kx), max_set(i - 1, kx) + 1):           #i-t nem választjukx
                cont.append(2)
            if len(cont) > 0:
                r = cont[random.randint(0, len(cont) - 1)]
                if r == 1:
                    e = -1
                    kx -= 1
                    zx -= i
                else:
                    e = 1
            else:
                e = 3
        else:
            print(kx, range(0, i + 1), zx, range(min_set(i, kx), max_set(i, kx) + 1))

        if ky in range(0, i + 1) and zy in range(min_set(i, ky), max_set(i, ky) + 1):
            cont = []
            if (zy - i) in range(min_set(i - 1, ky - 1), max_set(i - 1, ky - 1) + 1):  # i-t kyiválasztjuky
                cont.append(1)
            if zy in range(min_set(i - 1, ky), max_set(i - 1, ky) + 1):  # i-t nem választjuky
                cont.append(2)
            if len(cont) > 0:
                r = cont[random.randint(0, len(cont) - 1)]
                if r == 1:
                    f = -1
                    ky -= 1
                    zy -= i
                else:
                    f = 1
            else:
                f = 3
        else:
            print(ky, range(0, i + 1), zy, range(min_set(i, ky), max_set(i, ky) + 1))
        draw.line((x, y, x + u, y + v), fill=255, width=4, joint=None)
        i -= 1
        u += e
        v += f
        x += u
        y += v

random.seed()

for j in range(0, Params.turn):
    drawcircle(Params)
im.show()


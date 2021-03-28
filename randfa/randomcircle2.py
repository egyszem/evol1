# Jó random körök, és közülük a legsimábbak kiválasztva

import random
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw
@dataclass
class Params:
    width: int = 2000
    height: int = 1600
    m: int = 30
    n: int = 4 * m
    kx: int = n // 2
    ky: int = n // 2
    version: int = 0
    randseed: int = 0

def drawcircle(params: Params):

    def min_set(a, b):
        return b * (b + 1) // 2

    def max_set(a, b):
        return b * (2 * a - b + 1) // 2

    random.seed(params.randseed)

    x = params.width // 2
    y = params.height // 2
    u = random.randint(-params.m, params.m)
    v = random.randint(-params.m, params.m)
    zx = (params.n * u + params.n * (params.n + 1) // 2) // 2
    zy = (params.n * v + params.n * (params.n + 1) // 2) // 2
    kx = params.n // 2
    ky = params.n // 2
    i = params.n
    dmin = 1897.6
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
        draw.line((x, y, x + u, y + v), fill=255, width= 4 * params.version, joint=None)
        i -= 1
        u += e
        v += f
        x += u
        y += v
        dact = np.square(u) + np.square(v)
        if dact < dmin:
            dmin = dact

    return dmin

im = Image.new('L', (Params.width, Params.height))
draw = ImageDraw.Draw(im)
params = Params
circle_count = 10
trial_count = 10
for kk in range(0, circle_count):
    params.version = 0
    dmaxmin = 0
    for j in range(0, trial_count):
        random.seed()
        params.randseed = random.randint(0, 1000)
        d = drawcircle(params)
        if d > dmaxmin:
            dmaxmin = d
            seed = params.randseed
    params.version = 1
    params.randseed = seed
    d = drawcircle(params)
    #print(np.sqrt(dmaxmin), np.sqrt(d))
im.show()
im.save("images/random.korok3.jpg")
im.close()




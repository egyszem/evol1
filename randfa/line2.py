import random
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw

@dataclass
class Params:
    width: int = 2000
    height: int = 1600
    turn: int = 300
    angle: float = 0.0
    length = 10
    number_of_lines: int = 1
    order: int = 1
    random_seed: int = 0
    road: int = 100

im = Image.new('L', (Params.width, Params.height))
draw = ImageDraw.Draw(im)

def drawline(params: Params) -> None:
    half_width, half_height = params.width // 2, params.height // 2
    x, y = half_width, half_height
    u, v = int(params.length * np.cos(params.angle)), int(params.length * np.sin(params.angle))
    w, z = 0, 0
    i = 0

    while i < params.road:
        i += 1
        s = ""
        g = (np.abs(u) + 1) * (np.abs(u) + 2) // 2
        h = (np.abs(v) + 1) * (np.abs(v) + 2) // 2
        if x in range (g, params.width - g):
            w = random.choice((-1, 1))
        else:
            w = np.sign(half_width - x)
            s = s + "H"
        if y in range(h, params.height - h):
            z = random.choice((-1, 1))
        else:
            z = np.sign(half_height - y)
            s = s + "+V"
        u += w
        v += z
        draw.line((x, y, x + u, y + v), fill=255, width=4, joint="curved")
        x += u
        y += v

random.seed()
par  = Params
for k in range(0, par.turn):
    par.angle = 2 * np.pi * k / par.turn
    drawline(par)
im.show()

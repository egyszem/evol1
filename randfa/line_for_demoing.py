import random
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw

@dataclass
class Params:
    width: int = 2000
    height: int = 1600
    half_width: int = width // 2
    half_height: int = height // 2
    number_of_lines: int = 300
    route: int = 100
    order: int = 1
    random_seed: int = 0

def generate_lines(params: Params) -> Image:

    im = Image.new('L', (params.width, params.height))
    draw = ImageDraw.Draw(im)

    def drawline(params):
        x, y = params.half_width, params.half_height
        u, v = 0, 0
        w, z = 0, 0
        i = params.route
        while i > 0:
            i -= 1
            w += random.choice((-1, 1))
            z += random.choice((-1, 1))
            if params.order == 1:
                u = w
                v = z
            else:
                if params.order == 3:
                    g = u * (u + 1)
                    h = v * (v + 1)
                    if not x in range(g, params.width - g):
                        w = np.sign(params.half_width - x)
                    if not y in range(h, params.height - h):
                        z = np.sign(params.half_height - y)
                u += w
                v += z
            draw.line((int(x), int(y), int(x + u), int(y + v)), fill=255, width=4, joint="curved")
            x += u
            y += v

    for j in range(0, params.number_of_lines):
        drawline(params)
    return im




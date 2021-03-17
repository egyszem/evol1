from dataclasses import dataclass
import numpy as np
from PIL import Image
from PIL import ImageDraw
import numpy as np
import random

@dataclass
class Params:
    width: int = 1800
    height: int = 1600
    min_step: float = 2.81
    ray: float = 40
    number_of_rays: int = 20
    generation: int = 10
    seed: int = 0

seed = input("random seed: ")

def generate_lines(params: Params) -> Image:

    im = Image.new('L', (params.width, params.height))
    draw = ImageDraw.Draw(im)

    im = Image.new('L', (params.width, params.height))

    draw = ImageDraw.Draw(im)

    def lines(a):
        x, y = params.width / 2, params.height / 2
        u, v = params.ray * np.cos(a), params.ray * np.sin(a)
        delta_u, delta_v = 0, 0
        i = params.generation
        while (i > 0) and (x in range(0, params.width)) and (y in range(0, params.height)):
            i -= 1
            draw.line((int(x), int(y), int(x + u), int(y + v)), fill=255, width=4, joint="curved")
            u += delta_u
            v += delta_v
            delta_u += random.uniform(-1, 1) * params.min_step
            delta_v += random.uniform(-1, 1) * params.min_step

    for k in range(0, params.number_of_rays):
        random.seed(params.seed)
        lines(2 * k * np.pi / params.number_of_rays)

    return im


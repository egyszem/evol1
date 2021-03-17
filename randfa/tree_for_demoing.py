import random
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw


@dataclass
class Params:
    width: int = 1800
    height: int = 1600
    start_x: int = width // 2
    start_y: int = height - 1
    start_length: float = 100
    start_angle: float = 0.5 * np.pi
    min_length: float = 6.0
    length_log: float = np.log(start_length / min_length)
    contraction: float = 0.88
    delta_contraction: float = 0.06
    curvature_step: float = 0.25 * np.pi
    branching_probability: float = 0.18
    branching_angle: float = 0.45 * np.pi
    random_seed: int = 0


def generate_tree(params: Params) -> Image:

    im = Image.new('L', (params.width, params.height))
    draw = ImageDraw.Draw(im)

    def branch(x: int, y: int, length: float, angle: float):
        angle2 = 0.0
        while length > params.min_length:
            u = int(x + length * np.cos(angle))
            v = int(y - length * np.sin(angle))
            length = int((params.contraction + random.randint(0, 2) * params.delta_contraction) * length)
            curvature = random.uniform(-0.5, 0.5) * params.curvature_step
            angle2 = curvature
            angle += angle2
            draw.line((x, y, u, v), fill=255, width=int(0.4 * length), joint="curved")
            x = u
            y = v
            branching_angle = random.uniform(-1, 1) * params.branching_angle
            if random.random() < params.branching_probability:
                branch(x, y, length, angle + branching_angle)

    branch(params.start_x, params.start_y, params.start_length, params.start_angle)

    return im

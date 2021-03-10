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
    start_length: float = 100  # 1. paraméter: első szakasz hossza
    start_angle: float = 0.5 * np.pi
    min_length: float = 6.0  # 2. paraméter: legkisebb szakaszhossz -  2.0-nél nagyon bolyhos a vége, 10.0-nál már nem
    length_log: float = np.log(start_length / min_length)
    contraction: float = 0.88  # 3-4. paraméter: szakaszrövidülési kvóciens alsó határa és differencija
    delta_contraction: float = 0.06
    curvature_step: float = 0.25 * np.pi  # 5. paraméter: a szögváltozás változása,  nagyon érzékeny a konkrét paraméterekre
    branching_probability: float = 0.18
    branching_angle: float = 0.45 * np.pi  # parameter 6: max branching angle
    random_seed: int = 0


def generate_tree(params: Params) -> Image:
    # random.seed(params.random_seed)

    im = Image.new('L', (2000, 1600))
    draw = ImageDraw.Draw(im)

    def branch(x: int, y: int, length: float, angle: float):  # ágrajzolás
        # angle: másodfokban változik random
        angle2 = 0.0
        while length > params.min_length:
            u = int(x + length * np.cos(angle))
            v = int(y - length * np.sin(angle))
            length = int((params.contraction + random.randint(0, 2) * params.delta_contraction) * length)
            curvature = random.uniform(-0.5, 0.5) * params.curvature_step
            # angle2 += curvature
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

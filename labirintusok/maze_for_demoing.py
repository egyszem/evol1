import random
import time
from dataclasses import dataclass

import numpy as np
from PIL import Image
from PIL import ImageDraw


@dataclass
class Params:
    width: int = 64
    height: int = 48
    wall: int = 40
    line_width: int = 16
    radius: int = 20
    maze_version: int = 3
    show_version: int = 2
    wall_version: int = 1
    color: int = 192
    random_seed: int = 111


def generate_maze(params: Params) -> Image:
    """
    :rtype: object
    """
    random.seed(params.random_seed)
    im = Image.new('L', ((params.width + 1) * params.wall, (params.height + 1) * params.wall))
    draw = ImageDraw.Draw(im)
    maze = [[0] * (params.height + 1) for _ in range(params.width + 1)]

    def frame():
        for i in range(0, params.width + 1):
            maze[i][0] = 1
            maze[i][params.height] = 1
        for j in range(1, params.height):
            maze[0][j] = 1
            maze[params.width][j] = 1
        w = params.width // 2 - 1
        h = params.height // 2 - 1
        if random.randint(0, w + h) < w:
            maze[2 * random.randint(0, w) + 1][0] = 0
            maze[2 * random.randint(0, w + 1) - 1][params.height] = 0
        else:
            maze[0][2 * random.randint(0, h) + 1] = 0
            maze[params.width][2 * random.randint(0, w + 1) - 1] = 0

    def rand():
        for i in range(params.width):
            for j in range(params.height):
                if i % 2 == j % 2:
                    maze[i][j] = 1 - (i % 2)
                else:
                    maze[i][j] = random.randint(0, 1)

    def divide():
        def block(x1, y1, x2, y2):
            w = x2 - x1 - 2
            h = y2 - y1 - 2
            if w >= 2 and h >= 2:
                if random.randint(0, w + h) < w:
                    a = random.randrange(x1 + 2, x2, 2)
                    if random.choice((0, 1)) == 0:
                        for j in range(y1 + 2, y2):
                            maze[a][j] = 1
                    else:
                        for j in range(y1, y2 - 1):
                            maze[a][j] = 1
                    block(x1, y1, a, y2)
                    block(a, y1, x2, y2)
                else:
                    b = random.randrange(y1 + 2, y2, 2)
                    if random.choice((0, 1)) == 0:
                        for i in range(x1, x2 - 1):
                            maze[i][b] = 1
                    else:
                        for i in range(x1 + 2, x2):
                            maze[i][b] = 1
                    block(x1, y1, x2, b)
                    block(x1, b, x2, y2)

        block(0, 0, params.width, params.height)

    def divide_tomi():
        def block(x1, y1, x2, y2):
            w = x2 - x1 - 2
            h = y2 - y1 - 2
            if w >= 2 and h >= 2:
                if random.randint(0, w + h) < w:
                    a = random.randrange(x1 + 2, x2, 2)
                    for j in range(y1, y2):
                        maze[a][j] = 1
                    maze[a][random.randrange(y1 + 1, y2, 2)] = 0
                    block(x1, y1, a, y2)
                    block(a, y1, x2, y2)
                else:
                    b = random.randrange(y1 + 2, y2, 2)
                    for i in range(x1, x2):
                        maze[i][b] = 1
                    maze[random.randrange(x1 + 1, x2, 2)][b] = 0
                    block(x1, y1, x2, b)
                    block(x1, b, x2, y2)

        block(0, 0, params.width, params.height)

    def tree():
        def recursive_maze(x, y):
            z = []
            for (u, v) in ((x - 2, y), (x, y - 2), (x + 2, y), (x, y + 2)):
                if u in range(0, params.width + 1) and v in range(0, params.height + 1):
                    if maze[u][v] == 0:
                        z.append((u, v))
                        maze[u][v] = 1
            while len(z) > 0:
                r = random.randint(0, len(z) - 1)
                u, v = z[r]
                z.remove((u, v))
                maze[(x + u) // 2][(y + v) // 2] = 1
                recursive_maze(u, v)

        x = params.width // 2
        y = params.height // 2
        maze[params.width // 2][params.height // 2] = 1
        recursive_maze(x, y)

    def show():
        def draw_box(u, v):
            draw.rectangle((u * params.wall, v * params.wall, (u + 1) * params.wall - 1, (v + 1) * params.wall - 1),
                           fill=params.color, width=1)

        for i in range(params.width + 1):
            for j in range(params.height + 1):
                if maze[i][j] == 1:
                    draw_box(i, j)

    def show_line():

        def draw_side(u, v):
            if not (u % 2 == v % 2) and (maze[u][v] == 1):
                if v % 2 == 0:
                    draw.line(((u - 1) * params.wall, v * params.wall, (u + 1) * params.wall, v * params.wall),
                              fill=params.color, width=params.line_width, joint=None)
                else:
                    draw.line((u * params.wall, (v - 1) * params.wall, u * params.wall, (v + 1) * params.wall),
                              fill=params.color, width=params.line_width, joint=None)
            if (u % 2 == 0) and (v % 2 == 0):
                draw.ellipse((u * params.wall - params.radius, v * params.wall - params.radius,
                              u * params.wall + params.radius, v * params.wall + params.radius),
                             fill=params.color, outline=params.color, width=4)

        for i in range(params.width + 1):
            for j in range(params.height + 1):
                draw_side(i, j)

    def show_round():
        for u in range(0, params.width * params.wall):
            a = 2.0 * u / (params.width * params.wall) - 1.0
            for v in range(0, params.height * params.wall):
                b = 2.0 * v / (params.height * params.wall) - 1.0
                y = np.sqrt(np.square(a) + np.square(b))
                if y <= 1.0:
                    x = 0.25 + 0.5 * (np.arctan(b / (a + 0.000000001)) / np.pi + (1 - np.sign(a)) / 2)
                    k = maze[int(params.width * x)][int(params.height * y)]
                    im.putpixel((u, v), k * params.color)

    def show_round_matrix():
        maze2 = np.array(maze)
        a = np.arange(-1, 1 + 1 / params.width, 1 / params.width).reshape(-1, 1)
        b = np.arange(-1, 1 + 1 / params.height, 1 / params.height).reshape(-1, 1)

        a2 = a * a
        b2 = b * b

        x = (b @ (1 / (a + 1e-8)).T).T / np.pi + (1 - np.sign(a)) / 2
        x = (x * params.width).astype(int)
        y = np.tile(a2, [1, b.shape[0]]) + np.tile(b2, [1, a.shape[0]]).T
        y = y ** 0.5
        ix = y <= 1
        y = (y * params.height).astype(int)

        x = x[ix]
        y = y[ix]

        v = maze2[x, y] * params.color
        res = np.zeros_like(maze2)
        res[ix] = v

        print("hello")

    if params.maze_version == 0:
        rand()
        params.wall_version = 0
    if params.maze_version == 1:
        tree()
        params.wall_version = 1
    if params.maze_version == 2:
        divide()
        params.wall_version = 0
    if params.maze_version == 3:
        divide_tomi()
        params.wall_version = 0
    if params.wall_version == 0:
        frame()
    if params.show_version == 0:
        show()
    if params.show_version == 1:
        show_line()
    if params.show_version == 2:
        show_round()
    return im

if __name__ == '__main__':

    t_start = time.time()
    im1 = generate_maze(Params)
    delta = time.time() - t_start
    print(f"Execution took {delta:.1f} seconds")

    im1.show()
    im1.save("images/vonalas_rand_labi.jpg")

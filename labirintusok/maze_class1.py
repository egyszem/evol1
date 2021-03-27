import numpy as np
from PIL import Image
from PIL import ImageDraw
import random

WIDTH = 64
HEIGHT = 48
WALL = 40
RADIUS = 20
MAZE_VERSION = 2
SHOW_VERSION = 1
WALL_VERSION = 0
COLOR = 192
RANDOM_SEED = 111

random.seed(RANDOM_SEED)

im = Image.new('L', ((WIDTH + 1) * WALL, (HEIGHT + 1) * WALL))
draw = ImageDraw.Draw(im)

maze = [[0] * HEIGHT for _ in range(WIDTH)]
def __init__(self, width, height):
    self.width = WIDTH
    self.height = HEIGHT


def frame():
    for i in range(0, WIDTH):
        maze[i][0] = 1
        maze[i][HEIGHT - 1] = 1
    for j in range(0, HEIGHT):
        maze[0][j] = 1
        maze[WIDTH - 1][j] = 1
    w = WIDTH // 2 - 1
    h = HEIGHT // 2 - 1
    if random.randint(0, w + h) < w:
        maze[2 * random.randint(0, w) + 1][0] = 0
        maze[2 * random.randint(0, w) - 1][HEIGHT - 1] = 0
    else:
        maze[0][2 * random.randint(0, h) + 1] = 0
        maze[WIDTH - 1][2 * random.randint(0, w) - 1] = 0

def rand():
    for i in range(WIDTH):
        for j in range(HEIGHT):
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
    block(0, 0, WIDTH, HEIGHT)

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
    block(0, 0, WIDTH, HEIGHT)

def tree():
    def recursive_maze(x, y):
        z = []
        for (u, v) in ((x - 2, y), (x, y - 2), (x + 2, y), (x, y + 2)):
            if u in range(0, WIDTH) and v in range(0, HEIGHT):
                if maze[u][v] == 0:
                    z.append((u, v))
                    maze[u][v] = 1
        while len(z) > 0:
            r = random.randint(0, len(z) - 1)
            u, v = z[r]
            z.remove((u, v))
            maze[(x + u) // 2][(y + v) // 2] = 1
            recursive_maze(u, v)

    x = WIDTH // 2
    y = HEIGHT // 2
    self.maze[WIDTH // 2][HEIGHT // 2] = 1
    recursive_maze(x, y)

def show():
    def draw_box(u, v):
        draw.rectangle((u * WALL, v * WALL, (u + 1) * WALL - 1, (v + 1) * WALL - 1), fill=COLOR, width=1)
    for i in range(WIDTH):
        for j in range(HEIGHT):
            if maze[i][j] == 1:
                draw_box(i, j)

def show_line():
    def draw_side(u, v):
        if not (u % 2 == v % 2) and (maze[u][v] == 1):
            if v % 2 == 0:
                draw.line(((u - 1) * WALL, v * WALL, (u + 1) * WALL, v * WALL), fill = COLOR, width=16, joint=None)
            else:
                draw.line((u * WALL, (v - 1) * WALL, u * WALL, (v + 1) * WALL), fill = COLOR, width=16, joint=None)
        if (u % 2 == 0) and (v % 2 == 0):
            draw.ellipse((u * WALL - RADIUS, v * WALL - RADIUS, u * WALL + RADIUS, v * WALL + RADIUS), fill=COLOR, outline=COLOR, width=4)
        u = u

    for i in range(WIDTH):
        for j in range(HEIGHT):
            draw_side(i, j)

if MAZE_VERSION == 0:
    rand()
if MAZE_VERSION == 1:
    tree()
if MAZE_VERSION == 2:
    divide()
if MAZE_VERSION == 3:
    divide_tomi()
if WALL_VERSION == 0:
    frame()
if SHOW_VERSION == 0:
    show()
if SHOW_VERSION == 1:
    show_line()
im.show()
im.save("images/vonalas_divide2.jpg")





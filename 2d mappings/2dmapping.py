from dataclasses import dataclass
import numpy as np
from PIL import Image
from PIL import ImageDraw
import random

#x * y = u, x / y = v
# uv = x2 -> x = sqrt(uv), y = u / sqrt(uv) = sqrt(u / v)

@dataclass
class Params:
    width = 32
    height = 24
    wall = 50

im = Image.new("L", (Params.width * Params.wall, Params.height * Params.wall))

amax = - 1000
amin = 1000
bmax = - 1000
bmin = 1000
xmax = - 1000
xmin = 1000
ymax = - 1000
ymin = 1000

for u in range(0, Params.width * Params.wall):
    print(u)
    a = 2.0 * u / (Params.width * Params.wall) - 1.0
    amin = min(a, amin)
    amax = max(a, amax)
    for v in range(0, Params.height * Params.wall):
        k = 0
        b = 2.0 * v / (Params.height * Params.wall) - 1.0
        bmin = min(b, bmin)
        bmax = max(b, bmax)
        y = np.sqrt(np.square(a) + np.square(b))
        ymin = min(y, ymin)
        ymax = max(y, ymax)
        if y <= 1.0:
            x = 0.5 + np.arctan(b / (a + 0.000000001)) / np.pi + (1 - np.sign(a)) / 2
            xmin = min(x, xmin)
            xmax = max(x, xmax)
            k = (int(Params.width * x) + int(Params.height * y)) % 2
            im.putpixel((u, v), 255 * k)
print("amin, amax ", amin, amax)
print("bmin, bmax ", bmin, bmax)
print("xmin, xmax ", xmin, xmax)
print("ymin, ymax ", ymin, ymax)
im.show()
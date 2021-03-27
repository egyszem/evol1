from PIL import Image, ImageDraw, ImageFont
from PIL import BdfFontFile as font
import numpy as np
import random

WIDTH = 2000
HEIGHT = 1600
FORMA = 1 # vagy 0.. 2
VERSION = 1
SPREAD = 67 # 20 v. 67
N = WIDTH // SPREAD
M = HEIGHT // SPREAD
DENSITY = 0.95
FILLCOLOR = 0 # 0...255
DOT = 6
PEAK = 20.0
RADIUS = 600.0


im = Image.new('L', (WIDTH, HEIGHT))
draw = ImageDraw.Draw(im)
pos = [[(0, 0, 0)] * M for _ in range(N)]

def generate(forma):
    zmax = -1000.0
    zmin = 1000.0
    for i in range(0, N):
        for j in range(0, M):
            r = np.sqrt(np.square(SPREAD * i - WIDTH / 2) + np.square(SPREAD * j - HEIGHT / 2))
            if forma == 0:
                z = PEAK * np.cos(0.01 * r)
            elif forma == 1:
                if r < RADIUS:
                    z = 0.2 * np.sqrt(RADIUS * RADIUS - r * r)
                else:
                    z = 0.0
            elif forma == 2:
                z = 4  * PEAK * (np.cos(0.0025 * SPREAD * (i + j)) + np.cos(0.0025 * SPREAD * (i - j)))
            elif forma == 3:
                #z = -6 * PEAK * np.square(np.sin(0.002 * r))
                #z = 15 * PEAK /(0.000002 * r * r + 1.0)
                z = - 0.0002 * r * r
            zmax = max(z, zmax)
            zmin = min(z, zmin)
            pos[i][j] = (i * SPREAD, j * SPREAD, z)
    print("forma: ", FORMA, zmin, zmax)

def display(version):
    vmin = 10000
    adjx = 200
    adjy = -100
    for i in range(0, N):
        for j in range(0, M):
            (u, v, z) = pos[i][j]
            u += adjx + z
            v += adjy - z
            if version == 0:
                draw.ellipse((u - DOT, v - DOT, u + DOT, v + DOT), fill=255, outline=0, width=1)
            else:
                if j > 0:
                    (u1, v1, z1) = pos[i][j - 1]
                    u1 += adjx + z1
                    v1 += adjy - z1
                    draw.line((u, v, u1, v1), fill=255, width=3, joint=None)
                if i < N - 1:
                    (u2, v2, z2) = pos[i + 1][j]
                    u2 += adjx + z2
                    v2 += adjy - z2
                    draw.line((u, v, u2, v2), fill= 255, width=3, joint=None)
            if v < vmin:
                vmin = v - z
    print("vmin", vmin)
#
# for FORMA in range(0, 3):
#     generate(FORMA)
#     for VERSION in range(0, 2):
#         display(VERSION)
generate(3)
display(0)

im.show()
# if FORMA == 0:
#     im.save("cosinus_sugaras" + str(FORMA) + ".jpg")
# if FORMA == 1:
#     im.save("gömbös" + str(FORMA) + ".jpg")

print(WIDTH // SPREAD)
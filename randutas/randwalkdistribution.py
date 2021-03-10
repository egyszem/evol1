from PIL import Image, ImageDraw
import numpy as np
import random

w = 1800
h = 1200
w2 = w // 2
h2 = h // 2

im = Image.new('L', (w, h))

draw = ImageDraw.Draw(im)

random.seed()

side = 16
route_length = 1000
route_count = 1

dist = np.zeros((100, w, h), dtype=float)
dist[0][w2][h2] = 1.0

n = 100

np.set_printoptions(formatter={'float': '{: 0.3f}'.format})
#np.set_printoptions(precision=3, suppress=True)

for i in range(1, n):
    j1 = w2 - n // 2
    j2 = j1 + n
    if i > 0:
        for j in range(j1, j2):
            k1 = h2 - n // 2
            k2 = k1 + n
            for k in range(k1, k2):
                z = -dist[i - 1][j][k]
                for u in (j - 1, j, j + 1):
                    for v in (k - 1, k, k + 1):
                        z += dist[i - 1][u][v]
                z = z / 8.0
                dist[i][j][k] = z
    print (i, ".")
    #print(dist[i][w2 : w2 + i + 1, h2:  h2 + i + 1])

zzz = 0
nnn = 0
zmax = 0.0
for j in range(0, w):
    print(j)
    for k in range(0, h):
        sss = dist[n - 2][j][k]
        zzz += sss
        if sss > 0.0:
            nnn += 1
        if sss > zmax:
            zmax = sss
print("teljes valség: ", zzz, "nnn = ", n, w * h, "max ", zmax)
for j in range(0, w):
    for k in range(0, h):
        if (dist[99][j][k] > 0):
            im.putpixel((j, k), 127)
im.show()
#im.save("randwalkdistribution.jpg")




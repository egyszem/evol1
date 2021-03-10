from PIL import Image, ImageDraw
import numpy as np
import random

n = 1000000
smax = 0
smin = 0


def run(n):
    s = 0
    smax = 0
    smin = 0
    k = 0
    for i in range(0, n):
        d = random.choice((-1, 1))
        if d == -1:
            if s > smax:
                smax = s
                k += 1
        if d == 1:
            if s < smin:
                smin = s
                k += 1
        s += d
    return(smin, smax)

a = 0.0
b = 0.0
c = 0.0
d = 0.0
for i in range(0, 100):
    print(i)
    (smax, smin) = run(n)
    a += smax / n
    b += smax * smax
    c += smin / n
    d += smin * smin
print(a, np.sqrt(b - n * a * a) / n, c, np.sqrt(d - c * c) / n)
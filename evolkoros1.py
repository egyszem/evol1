from PIL import Image as im
import numpy as np
import random

random.seed()


def main(w, h, n):
    im1 = im.new('1', (w, h))
    [x, y] = [w // 2, h // 2]
    im1.putpixel([x, y], 1)
    k = 0
    for _ in range(n):
        x = random.randint(1, w - 2)
        y = random.randint(1, h - 2)
        if im1.getpixel((x, y)) == 1:
            z = []
            for u in range(x - 1, x + 2):
                for v in range(y - 1, y + 2):
                    if im1.getpixel((u, v)) == 0:
                        z.append([u, v])
            if len(z) > 0:
                r = random.randint(0, len(z) - 1)
                [u, v] = z[r]
                im1.putpixel([u, v], 1)
        if 100 * _ / n > k:
            print (k)
            k += 1
    im1.show()

n = 10000000
main(600, 400, n)

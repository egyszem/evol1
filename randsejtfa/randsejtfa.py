from PIL import Image as im, ImageDraw as imdraw
import numpy as np
import random

random.seed()
version = random.randint(1, 2)


def main(w, h, n):
    im1 = im.new('1', (w, h))
    x = w // 2
    y = h - 1
    pointlist = [(x, y)]
    im1.putpixel((x, y), 1)
    while len(pointlist) in range(1, n):
        # while len(pointlist) > 0 and len(pointlist) < route_count:
        r = random.randint(0, len(pointlist) - 1)
        x, y = pointlist[r]
        rr = random.randint(0, h)
        if rr < y:
            u = x
            v = y - 1
        else:
            if version == 1:
                u = x + 2 * random.randint(0, 1) - 1
                v = y
            else:
                z = []
                for (u, v) in [(x - 1, y), (x + 1, y)]:
                    if im1.getpixel((u, v)) == 0:
                        z.append((u, v))
                if len(z) > 0:
                    (u, v) = z[random.randint(0, len(z) - 1)]
        if u in range(0, w) and v in range(0, h):
            if im1.getpixel((u, v)) == 0:
                pointlist.append((u, v))
                im1.putpixel((u, v), 1)
            else:
                pointlist.remove((x, y))

    im1.show()
    im1.save("randsejtfa_sovany11.jpg")

w = 1000
main(w, w, 1600)

from PIL import Image as im
from PIL import ImageDraw
import numpy as np
import random
imn = im.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)


random.seed()


def main(w, h, n):
    im1 = im.new('1', (w, h))
    blocklist = [(0, 0, w, h, w * h)]
    while len(blocklist) > 0:
        r = random.randint(0, len(blocklist) - 1)
        (a, b, c, d, e) = blocklist[r]
        for u in range(x - 1, x + 2):
            for v in range(y - 1, y + 2):
                if u >= 0 and u < w and v >= 0 and v < h and im1.getpixel((u, v)) == 0:
                    z.append((u, v))
        if len(z) > 0:
            r = random.randint(0, len(z) - 1)
            (u, v) = z[r]
            blocklist.append((u, v))
            im1.putpixel((u, v), 1)
        else:
            blocklist.remove((x, y))
    im1.show()


w = 1000
main(w, w, 8000)

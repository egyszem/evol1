from PIL import Image as im
import numpy as np
import random

random.seed()

def main(w, h, n):
    remove = 0
    add = 0
    im1 = im.new('L', (w, h))
    x, y = w // 2, h // 2
    pointlist = [(x, y)]
    im1.putpixel((x, y), 1)
    while len(pointlist) < n and len(pointlist) > 0:
        print((100 * len(pointlist) / n) // 1)
        r = random.randint(0, len(pointlist) - 1)
        (x, y) = pointlist[r]
        z = []
        for u in range(x - 1, x + 2):
            for v in range(y - 1, y + 2):
                if u in range(0, w) and v in range (0, h) and  (im1.getpixel((u, v)) == 0):
                    z.append((u, v))
        if len(z) > 0:
            r = random.randint(0, len(z) - 1)
            (u, v) = z[r]
            pointlist.append((u, v))
            im1.putpixel((u, v), 255)
            add += 1
        else:
            pointlist.remove((x, y))
            im1.putpixel((u, v), 127)
            remove += 1
    im1.show()
    #im1.save("randkoros3.jpg")
    print ("remove ", remove, ", add ", add)


w = 1000
main(w, w, 8000)

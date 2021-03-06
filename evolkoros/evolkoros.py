from PIL import Image as im
import numpy as np
import random

random.seed()

def main(w, h, n):
    def rand_neighbor(xx, yy):
        z = []
        for xxx in range(xx - 1, xx + 2):
            for yyy in range(yy - 1, yy + 2):
                if xxx in range(0, w) and yyy in range (0, h) and  (im1.getpixel((xxx, yyy)) == 0):
                    z.append((xxx, yyy))
        if len(z) > 0:
            r = random.randint(0, len(z) - 1)
            return z[r]
        else:
            return (xx, yy)

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
        (u, v) = rand_neighbor(x, y)
        if not (u, v) == (x, y):
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

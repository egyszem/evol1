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

side = 6
route_length = 1000
route_count = 10000

point_list =[]
a = [0, 0, -side, side]
b = [-side, side, 0, 0]

def route():
    x, y = w2, h2
    for _ in range(0, route_length):
        r = random.randint(0, 3)
        u, v = x + a[r], y + b[r]
        draw.line(((x, y, u, v)), fill=128, width= 2, joint="curved")
        x, y = u, v
    if (x, y) not in point_list:
        point_list.append((x, y))
    return ((x, y))


def main():
    counter = 0
    for i in range(0, route_count):
        (x, y) = route()
        z = int(100 * i / route_count)
        if z > counter:
            counter = z
            print(counter)

def evaluate():
    outer_point_list = []
    zmax = 0
    for (x, y) in point_list:
        z = 0
        for u in (x - side, x, x + side):
            for v in (y - side, y, y + side):
                if u in range(0, w) and v in range(0, h) and (u, v) in point_list:
                    z += 1
        if z < 3:
            outer_point_list.append((x, y))
        if z > zmax:
            zmax = z

    s = 0.0
    s2 = 0.0
    for (x, y) in outer_point_list:
        #draw.arc(((x - 2, y - 2), (x + 2, y + 2)), 0, 360, fill=255, width=2)
        t = (np.sqrt((x - w2) * (x - w2) + (y - h2) * (y - h2)))
        s += t
        s2 += t * t
    m = len(outer_point_list)
    s = s / m
    s2 = s2 / m
    print("average ", s, "squared average ", s * s, "average squares ", s2)
    sd = np.sqrt(s2 - s * s)
    print("dispersion ", sd)
    for aa in (s - sd, s, s + sd):
        if aa == s:
            draw.arc(((w2 - aa, h2 - aa), (w2 + aa, h2 + aa)), 0, 360, fill=255, width=4)
        else:
            draw.arc(((w2 - aa, h2 - aa), (w2 + aa, h2 + aa)), 0, 360, fill=255, width=2)

main()
evaluate()

im.show()
im.save("randutas1 side 6 length 1000 count 10000.jpg")




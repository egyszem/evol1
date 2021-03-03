from PIL import Image, ImageDraw
import numpy as np
import random

w = 1600
h = 1200
w2 = w // 2
h2 = h // 2

im = Image.new('L', (w, h))

draw = ImageDraw.Draw(im)

random.seed()

side = 6
route_length = 1000
n = 10000

point_list =[]

def route():
    x, y = w2, h2
    for _ in range(0, route_length):
        u, v = x, y
        r = random.randint(0, 3)
        if r == 0:
            u += side
        if r == 1:
            v  += side
        if r == 2:
            u -= side
        if r == 3:
            v -= side
        draw.line(((x, y, u, v)), fill=128, width= 1, joint="None")
        x, y = u, v
    if (x, y) in point_list:
        return(0)
    else:
        point_list.append((x, y))
        return (np.sqrt((x - w2) * (x - w2) + (y - h2) * (y - h2)))


s = 0.0
s2 = 0.0
counter = 0
for i in range(0, n):
    t = route()
    z = int(100 * i / n)
    if z > counter:
        counter = z
        print(counter,)
    s += t
    s2 += t * t

m = len(point_list)
print("point_list_length ", m)
s = s / m
s2 = s2 / m
print("average ", s, "squared average ", s * s, "average squares ", s2 )
sd = np.sqrt(s2 - s * s )
print("dispersion ", sd)
for a in (s - sd, s, s + sd):
    if a == s:
        color = 255
        breadth = 3
    else:
        color = 127
        breadth = 1
    draw.arc(((w2 - a, h2 - a), (w2 + a, h2 + a)), 0, 360, fill=255, width=breadth)
im.show()
im.save("randutas_old.jpg")



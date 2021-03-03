# ez a jó, ezzel csináltam a rajzokat -- csak most rekurzív függvényhívással

from PIL import Image, ImageDraw
import numpy as np
import random

im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
w = 1800
h = 1600
n = 10
q = 0.88                        # 1. paraméter: szakaszrövidülési kvóciens alsó határa
random.seed()
startx = w // 2
starty = h - 1
startlength = 80.0             # 2. paraméter: 1. szakasz hossza
startangle = 0.5 * np.pi

def branch(actualx, actualy, actuallength, actualangle):  # ágrajzolás
    x = actualx
    y = actualy
    l = actuallength
    angle = actualangle  # a szakasz szöge, másodfokban változik random
    angle2 = 0.0 # a szakasz szögváltozása
    while (l > 4.0):
    # egymás után fűzött szakaszok # 2.0-nél nagyon bolyhos a vége, 10.0-nál már nem
    # 3. paraméter: legkisebb szakaszhossz
        u = int(x + l * np.cos(angle))
        v = int(y - l * np.sin(angle))
        l = int((q + 0.06 * random.randint(0,2)) * l)  # 4. paraméter: szakaszrövidülési kvóciens intervalluma: itt q = 0.88...0.94
        curvature = 0.000035 * (random.randint(0, 1000) - 501) * np.pi
        # kvázi görbület: a szögváltozás változása,  nagyon érzékeny a konkrét paraméterekre / = 0.0175 Pi = 3.15 fok
        # 5. paraméter: szakaszgörbület, itt 0.0175 Pi
        angle2 += curvature
    angle += angle2
        draw.line(((x, y, u, v)), fill=255, width= int(0.4 * l), joint="curved")
        x = u
        y = v
        if (random.randint(0, 100) < 27) and (random.randint(0, 45) > np.log(l)):
        # 6. paraméter: elágazási valószínűség: itt 27% and (0.9... 1,0)) -- különös feltétel
            # 7. paraméter: elágazási szög, itt - Pi/4 ... Pi/4
            branch(x, y, l, angle + .025 * (random.randint(0, 20) - 10) * np.pi)
    return()

branch(startx, starty, startlength, startangle)
im.show()
im.save("randagasfa1recursive1.jpg")

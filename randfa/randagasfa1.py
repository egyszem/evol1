# ez a jó, ezzel csináltam a rajzokat

from PIL import Image, ImageDraw
import numpy as np
import random

im = Image.new('L', (1800, 1600))

draw = ImageDraw.Draw(im)
w = 1800
h = 1600
n = 10
q = 0.88                        # 1. paraméter: szakaszrövidülési kvóciens alsó határa
random.seed()
startx = w // 2
starty = h - 1
startlength = 100.0             # 2. paraméter: 1. szakasz hossza
startangle = 0.5 * np.pi
branchlist = [(startx, starty, startlength, startangle)]  # kepernyő alja-közepen 100 hosszú függőleges szakasz felvétele a listára

def branch(actualx, actualy, actuallength, actualangle):  # ágrajzolás
    branchlist.remove((actualx, actualy, actuallength, actualangle))  # az aktuálisan kiválasztott ágat már törölhetjük a listáról
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
            branchlist.append((x, y, l, angle + .025 * (random.randint(0, 20) - 10) * np.pi)) # az adott szakasztól kiinduló új ág kezdőpotját rögzítjük a listán
            # 7. paraméter: elágazási szög, itt - Pi/4 ... Pi/4

while len(branchlist) > 0: # a listáról levett ágakat megrajzoljuk
    r = random.randint(0, len(branchlist) - 1)
    (startx, starty, startlength, startangle) = branchlist[r]
    branch(startx, starty, startlength, startangle)
print(len(branchlist))
im.show()
im.save("randagasfa112.jpg")

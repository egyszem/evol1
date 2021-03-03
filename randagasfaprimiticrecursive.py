from PIL import Image, ImageDraw
import numpy as np
import random

im = Image.new('L', (1800, 1600))

draw = ImageDraw.Draw(im)
w = 1800
h = 1600
q = 0.7     # 1. paraméter: ágrövidülési koefficiens
diff = 0.16 * np.pi   # 2. paraméter: új ágak fisz szögelfordulása
random.seed()
startx = w // 2
starty = h - 1
startlength = 800.0  #3. paraméter: kezdeti ághossz
startangle = 0.5 * np.pi

def branch(actualx, actualy, actuallength, actualangle, actualdiff = diff):
    x = actualx
    y = actualy
    l = actuallength
    angle = actualangle
    diff1 = actualdiff
    u = int(x + np.cos(angle) * l)
    v = int(y - np.sin(angle) * l)
    # branchlist.remove((actualx, actualy, actuallength, actualangle, diff1)) # kivalasztott ag torlese a listarol
    draw.line(((x, y, u, v)), fill=255, width=10, joint="None")
    branchnumber = random.randint(1, 3)  # 4. paraméter: max leágazásszám
    if random.randint(0, 1) == 0:  # random jobbra vagy balra?
        diff1 = -diff1
    l = int(q * l)
    r = 0
    if l > 15:  # 5. paraméter: minimális ághossz
        for i in range(0, branchnumber):
            r = random.randint(r, l)
            diff1 = -diff1
            u = int(x + np.cos(angle) * r)
            v = int(y - np.sin(angle) * r)
            #branchlist.append((u, v, l, angle + diff1, diff1))  # uj agak kiindulopontjainak felvetele a listara
            branch(u, v, l, angle + diff1, diff1)
    return


while len(branchlist) > 0:
    r = random.randint(0, len(branchlist) - 1)
    (startx, starty, startlength, startangle, diff1) = branchlist[r]  # random agkiindulas valasztasa
    branch(startx, starty, startlength, startangle, diff1)  # ag megrajzolasa
print(len(branchlist))
im.show()
im.save("randagasfaprimitiv4.jpg")

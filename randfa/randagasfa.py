from PIL import Image, ImageDraw
import numpy as np
import random

im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
w = 1800
h = 1600
n = 10
q = 0.92

random.seed()

def drawbranch(a, b, c, d, strength):
    draw.line(((a, b, c, d)), fill=255, width=strength, joint="curved")


# draw.line(((0, 1600), (500, 400), (1800, 1400), (2000, 0)), fill=255, width=40, joint="curved")
first_branch = (w // 2, h - 1, w // 2, h - 100, 100)
branch_list = [first_branch]

drawbranch(first_branch[0], first_branch[1], first_branch[2], first_branch[3], first_branch[4])
print (branch_list[0])
branch_count = 0
while (len(branch_list)) in range(0, n):
    r = random.randint(0, len(branch_list) - 1)
    print("r ", r)
    (x1, y1, x2, y2, strength) = branch_list[r]
    print(x1, y1, x2, y2, strength)
    l = int(np.sqrt((x2 - x1) * (x2 - x1) * (y2 - y1) * (y2 - y1)))
    if random.randint(0, 10) >= 0:
        branch_list.remove(branch_list[r])
    if (x1 in range(0, w)) and (y1 in range(0, h)) and (x2 in range(0, w)) and (y2 in range(0, h)) and (l > 0):
        drawbranch(x1, y1, x2, y2, strength)
        branch_count += 1
        x1 = x2
        y1 = y2
        strength = int(q * strength)
        l = int(q * l)
        angle = (100 - l) * np.pi * (random.randint(0, 10) - 5) / 500
        co = np.cos(angle)
        si = np.sin(angle)
        x2 += int(l * co)
        y2 += int(l * si)
        branch_list.append((x1, y1, x2, y2, strength))
        print("listlength ", len(branch_list))
        drawbranch(x1, y1, x2, y2, strength)
print(branch_list)
del draw
im.show()

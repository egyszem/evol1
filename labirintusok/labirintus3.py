import numpy as np
import matplotlib.pyplot as plt
import random

gap_width = 40  # min. folyososzelesseg
wall_width = 40  # falvastagsag
minimalblock_width = 2 * gap_width + wall_width  # minimalis blokkoldal
width = 1999
height = 1599
block = (0, height, 0, width)
blocklist = [block]
print(len(blocklist), 'listahossz')
wall_count = 0
max_list_hossz = 1


def randside(a, b):
    return random.randint(a + gap_width, b - gap_width - wall_width + 1)


def draw_block(canvas, block):
    canvas[block[0]: block[1], block[2]: block[3]] = 1


canvas = np.zeros((height, width))

while len(blocklist) > 0:
    wall_count += 1
    if len(blocklist) > max_list_hossz:
        max_list_hossz = len(blocklist)
    r = random.randint(0, len(blocklist) - 1)
    (a, b, c, d) = blocklist[r]  # bigblock torlese a listarol
    blocklist.remove((a, b, c, d))
    print(wall_count, " bigblock: ", a, b, c, d, " -- ", )
    # if random.randint(0, 1) == 0:  # a bigblock fuggoleges ketteosztasa
    if random.randint(0, b + d - a - c) < b - a:
        divide = randside(a, b)
        print('horizontal divide = ', divide)
        leftblock = (a, divide, c, d)
        rightblock = (divide + wall_width, b, c, d)
        if divide - a > minimalblock_width:  # ha eleg szeles
            blocklist.append(leftblock)  # leftblock felvetele a listara
        if b - divide - wall_width > minimalblock_width:  # ha eleg szeles
            blocklist.append(rightblock)  # rightblock felvetele a listara
        if random.randint(0, 1) == 0:  # fal alulrol
            middleblock = (divide, divide + wall_width, c, d - gap_width)
        else:  # fal felulrol
            middleblock = (divide, divide + wall_width, c + gap_width, d)
        print('middle:', middleblock)
        draw_block(canvas, middleblock)
        print('left ', leftblock,
              'middle ', middleblock,
              'right ', rightblock)
    else:  # a bigblock vizszintes ketteosztasa
        divide = randside(c, d)
        print('vertical divide = ', divide)
        lowerblock = (a, b, c, divide)
        upperblock = (a, b, divide + wall_width, d)
        if divide - c > minimalblock_width:  # ha eleg szeles
            blocklist.append(lowerblock)  # lowerblock felvetele a listara
        if d - divide - wall_width > minimalblock_width:  # ha eleg szeles
            blocklist.append(upperblock)  # upperblock felvetele a listara
        if random.randint(0, 1) == 0:  # fal balrol
            middleblock = (a + gap_width, b, divide, divide + wall_width)
        else:  # fal jobbrol
            middleblock = (a, b - gap_width, divide, divide + wall_width)
        print('lower ', lowerblock,
              'middle ', middleblock,
              'upper ', upperblock)
        draw_block(canvas, middleblock)

print ("listmax: ", max_list_hossz)

plt.imshow(canvas)
plt.axis("off")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
import random
class BlockCoords:
    def __init__(self, y_bottom, y_top, x_left, x_right):
        self.y_bottom = y_bottom
        self.y_top = y_top
        self.x_left = x_left
        self.x_right = x_right
gap_width = 40  # min. folyososzelesseg
wall_width = 20  # falvastagsag
minimalblock_width = 2 * gap_width + wall_width
width = 999
height = 799
block = BlockCoords(0, height, 0, width)
blocklist = [block]
print(len(blocklist), 'listahossz')

def randside(a, b):
    return random.randint(a + gap_width, b - gap_width - wall_width)

def draw_block(canvas, rect):
    canvas[rect.y_top: rect.y_bottom + 1, rect.x_left: rect.x_right + 1] = 1

canvas = np.zeros((height,width))

wall_count = 1

while len(blocklist) > 0:
    r = random.randint(0, len(blocklist) - 1)
    bigblock = blocklist[r] # bigblock torlese a listarol
    print('big: ', bigblock.x_left, bigblock.x_right, bigblock.y_bottom, bigblock.y_top)
    blocklist.remove(bigblock)
    print('big: ', bigblock.x_left, bigblock.x_right, bigblock.y_bottom, bigblock.y_top)
    wall_count = ++1
    print(wall_count, ' wall')
    if random.randint(0, 1) == 0: # a bigblock fuggoleges ketteosztasa
        divide = randside(bigblock.x_left, bigblock.x_right)
        print ('horizontal divide = ', divide)
        leftblock = bigblock
        leftblock.x_right = divide
        middleblock = bigblock
        middleblock.x_left = leftblock.x_right + 1
        middleblock.x_right = leftblock.x_right + wall_width
        rightblock = bigblock
        rightblock.x_left = leftblock.x_right + wall_width + 1
        print ('l ', leftblock.x_left, leftblock.x_right, leftblock.y_bottom, leftblock.y_top,
               'number_of_lines ', middleblock.x_left, middleblock.x_right, middleblock.y_bottom, middleblock.y_top,
               'r ', rightblock.x_left, rightblock.x_right, rightblock.y_bottom, rightblock.y_top)
        if leftblock.x_right - leftblock.x_left > minimalblock_width: # ha eleg szeles
            blocklist.append(leftblock) # leftblock felvetele a listara
            wall_count = ++1
        if rightblock.x_right - rightblock.x_left > minimalblock_width: # ha eleg szeles
            blocklist.append(rightblock) # rightblock felvetele a listara
            wall_count = ++1
        if random.randint(0,1) == 0: # fal alulrol
            middleblock.y_top = -- gap_width
        else:   # fal felulrol
            middleblock.y_bottom = ++ gap_width
        draw_block(canvas, middleblock)
    else: # a bigblock vizszintes ketteosztasa
        divide = randside(bigblock.y_bottom, bigblock.y_top)
        print('vertical divide = ', divide)
        lowerblock = bigblock
        lowerblock.y_top = randside(bigblock.y_bottom, bigblock.y_top)
        middleblock = bigblock
        middleblock.y_bottom = lowerblock.y_top + 1
        middleblock.y_top = lowerblock.y_top + wall_width
        upperblock = bigblock
        upperblock.y_bottom = lowerblock.y_top + wall_width + 1
        print ('l ', lowerblock.x_left, lowerblock.x_right, lowerblock.y_bottom, lowerblock.y_top,
               'number_of_lines ', middleblock.x_left, middleblock.x_right, middleblock.y_bottom, middleblock.y_top,
               'u ', upperblock.x_left, upperblock.x_right, upperblock.y_bottom, upperblock.y_top)
        if lowerblock.y_top - lowerblock.y_bottom > minimalblock_width: # ha eleg szeles
            blocklist.append(lowerblock) # lowerblock felvetele a listara
            wall_count = ++1
        if upperblock.y_top - upperblock.y_bottom > minimalblock_width: # ha eleg szeles
            blocklist.append(upperblock) # upperblock felvetele a listara
            wall_count = ++1
        if random.randint(0,1) == 0: # fal balrol
            middleblock.x_right = -- gap_width
        else:   # fal jobbrol
            middleblock.x_left = ++ gap_width
        draw_block(canvas, middleblock)
plt.imshow(canvas)
plt.show()



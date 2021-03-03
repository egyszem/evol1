from typing import Tuple

import numpy as np
import matplotlib.pyplot as plt
import random


class Block:
    def __init__(self, x_left: int, x_right: int, y_bottom: int, y_top: int):
        self.x_left = x_left
        self.x_right = x_right
        self.y_bottom = y_bottom
        self.y_top = y_top


gap_width = 40  # min. folyososzelesseg
width = 1999
height = 1599
block = Block(0, width, 0, height)
block_list = [block]
canvas = np.zeros((height, width))
wall_count = 0
max_list_hossz = 1

def is_valid(lower, upper) -> bool:
    return upper - lower > min_block_width


def split_side(a: int, b: int) -> Tuple:
    divide = random.randint(a + gap_width, b - gap_width - wall_width)
    return (a, divide, divide, divide + wall_width, divide + wall_width, b,
            is_valid(a, divide), is_valid(divide + wall_width, b))

def draw_block(canvas: np.ndarray, block) -> None:
    canvas[block.y_bottom: block.y_top, block.x_left: block.x_right] = 1


def split_block(block) -> None:
    case = random.randint(0, 3)
    if case == 0: # balrol
        sides = split_side(block.x_left, block.x_right)
        left_big_block = Block(sides[0], sides[1], block.y_bottom, block.y_top)
        if sides[6]:
            block_list.append(left_big_block)
        right_big_block = Block(sides[2], sides[5], block.y_bottom, block.y_top)
        sides = split_side(block.y_bottom, block.y_top)
        lower_block = Block(right_big_block.x_left, right_big_block.x_right, sides[0], sides[1])
        if sides[6]:
            block_list.append(lower_block)
        upper_block = Block(right_big_block.x_left, right_big_block.x_right, sides[4], sides[5])
        if sides[7]:
            block_list.append(upper_block)
        middle_block = Block(right_big_block.x_left, right_big_block.x_right, sides[2], sides[3])
    if case == 1:  # alulrol
        sides = split_side(block.x_left, block.x_right)
        left_big_block = Block(sides[0], sides[1], block.y_bottom, block.y_top)
        if sides[6]:
            block_list.append(left_big_block)
        right_big_block = Block(sides[2], sides[5], block.y_bottom, block.y_top)
        sides = split_side(block.y_bottom, block.y_top)
        lower_block = Block(right_big_block.x_left, right_big_block.x_right, sides[0], sides[1])
        if sides[6]:
            block_list.append(lower_block)
        upper_block = Block(right_big_block.x_left, right_big_block.x_right, sides[4], sides[5])
        if sides[7]:
            block_list.append(upper_block)
        middle_block = Block(right_big_block.x_left, right_big_block.x_right, sides[2], sides[3])
    if case == 2: # folulrol
        sides = split_side(block.x_left, block.x_right)
        right_big_block = Block(sides[2], sides[5], block.y_bottom, block.y_top)
        if sides[7]:
            block_list.append(right_big_block)
        left_big_block = Block(sides[0], sides[1], block.y_bottom, block.y_top)
        sides = split_side(block.y_bottom, block.y_top)
        lower_block = Block(left_big_block.x_left, left_big_block.x_right, sides[0], sides[1])
        if sides[6]:
            block_list.append(lower_block)
        upper_block = Block(left_big_block.x_left, left_big_block.x_right, sides[4], sides[5])
        if sides[7]:
            block_list.append(upper_block)
        middle_block = Block(left_big_block.x_left, left_big_block.x_right, sides[2], sides[3])

    draw_block(canvas, middle_block)
    block_list.remove(block)


while len(block_list) > 0:
# while wall_count < 26:
    wall_count += 1
    r = random.randint(0, len(block_list) - 1)
    if len(block_list) > max_list_hossz:
        max_list_hossz = len(block_list)
    block = block_list[r]  # random block valasztasa a listarol
    print(wall_count, ".block: ", block.x_left, block.x_right, block.y_bottom, block.y_top)
    wall_width = random.randint(10, 60)  # falvastagsag
    min_block_width = 2 * gap_width + wall_width  # minimalis blokkoldal
    if is_valid(block.x_left, block.x_right) and is_valid(block.y_bottom, block.y_top):
        split_block(block)
    else:
        block_list.remove(block)

print ("listmax: ", max_list_hossz)
plt.imshow(canvas)
plt.axis("off")
plt.show()

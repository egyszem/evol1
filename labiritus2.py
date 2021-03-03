import numpy as np
import matplotlib.pyplot as plt
import random

gap_width = 10  # min. folyososzelesseg
wall_width = 4  # falvastagsag

class RectCoords:
    def __init__(self, y_bottom, y_top, x_left, x_right):
        self.y_bottom = y_bottom
        self.y_top = y_top
        self.x_left = x_left
        self.x_right = x_right

def rndside(a, b):
    return random.randint(a + gap_width, b - gap_width - wall_width)


def leftwall(rect):
    y_bottom = rndside(rect.y_bottom, rect.y_top)
    return RectCoords(y_bottom, y_bottom + wall_width, rect.x_left, rect.x_right)



def topwall(x_left, y_bottom, x_right, y_top):
    return rndside(x_left, x_right), y_bottom + gap_width, x_left + wall_width, y_top


def rightwall(x_left, y_bottom, x_right, y_top):
    return x_left + gap_width, rndside(y_bottom, y_top), x_right, y_bottom + wall_width


def bottomwall(x_left, y_bottom, x_right, y_top):
    return rndside(x_left, x_right), y_bottom, x_left + wall_width, y_top - gap_width


def draw_rectangle(canvas, rect):
    canvas[rect.y_top: rect.y_bottom + 1, rect.x_left: rect.x_right + 1] = 1

canvas = np.zeros((100,100))

rect = RectCoords(0, 99, 0, 99)
wall_rect = leftwall(rect)

# print(x_left, y_bottom, x_right, y_top)
draw_rectangle(canvas, wall_rect)

plt.imshow(canvas)
plt.show()



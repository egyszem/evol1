# this produced the images, only this time with recursive function calls

from PIL import Image, ImageDraw
import numpy as np
import random

im = Image.new('L', (2000, 1600))

draw = ImageDraw.Draw(im)
w = 1800
h = 1600
n = 10
q = 0.88                        # parameter 1: section contraction rate
seed = input("random seed: ")
random.seed(seed)
startx = w // 2
starty = h - 1
startlength = 80.0             # parameter 2. starting section
startangle = 0.5 * np.pi

def branch(actualx, actualy, actuallength, actualangle):
# draws a branch recursively
    x = actualx
    y = actualy
    l = actuallength
    angle = actualangle  # section angle changing in second order
    angle2 = 0.0 # amount of section angle change
    while (l > 4.0):
    # length of minimal section – with 2.0 rather fuzzy, with 10 clean
    # parameter 3: minimal section
        u = int(x + l * np.cos(angle))
        v = int(y - l * np.sin(angle))
        l = int((q + 0.06 * random.randint(0,2)) * l)
	# parameter 4: range for section contraction rate.
	# here: q = 0.88...0.94
        curvature = 0.0175 * random.uniform(-1.0, 1.0) * np.pi
        # quasi curvature: change of angle change
	# rather sensitive. actual value: = 0.0175 Pi = 3.15 degrees
    	# parameter 5: section curvature, actually 0.0175 Pi
        angle2 += curvature
        angle += angle2
        draw.line(((x, y, u, v)), fill=255, width= int(0.4 * l), joint="curved")
        x = u
        y = v
        if (random.randint(0, 100) < 27) and (random.randint(0, 45) > np.log(l)):
        # parameter 6: branching probability: here 0.27 AND (0.9... 1,0))
	# a strange condition
       	# parameter 7: branching angle, actual value = - Pi/4 ... Pi/4
            branch(x, y, l, angle + .025 * (random.randint(0, 20) - 10) * np.pi)
    return()

branch(startx, starty, startlength, startangle)
im.show()
im.save("images/randagasfarecursive_{seed}.jpg")

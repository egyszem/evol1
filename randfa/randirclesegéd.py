import random
import numpy as np
from PIL import Image
from PIL import ImageDraw

s = []

def carryout():
    def min_set(a, b):
        return b * (b + 1) // 2

    def max_set(a, b):
        return b * (2 * a - b + 1) // 2

    n = 1000
    k = 500
    i = n
    z = random.randint(min_set(n, k), max_set(n, k) + 1)
    print(z)
    while i > 0:
        if k in range(0, i + 1) and z in range(min_set(i, k), max_set(i, k ) + 1):
            cont = []
            if (z - i) in range(min_set(i - 1, k - 1), max_set(i - 1, k - 1) + 1): #i-t kiválasztjuk
                cont.append(1)
            if z in range(min_set(i - 1, k), max_set(i - 1, k) + 1):           #i-t nem választjuk
                cont.append(2)
            if len(cont) > 0:
                r = cont[random.randint(0, len(cont) - 1)]
                if r == 1:
                    s.append(i)
                    k -= 1
                    z -= i
        i -= 1

carryout()
j = 0
for i in s:
    j += i
print(j)

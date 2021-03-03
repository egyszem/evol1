import numpy as np
import matplotlib.pyplot as plt

img = np.random.rand(10, 12)
img = np.zeros((100,80))
img[10,10] = 1
plt.imshow(img)
plt.show()

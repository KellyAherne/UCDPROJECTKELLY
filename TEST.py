import os
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5, 6, 7]
y = [160, 167, 17, 130, 120, 40, 105, 70]
fig, ax = plt.subplots()
width = 0.75
ind = np.arange(len(y))

ax.barh(ind, y, width, color="green")

for i, v in enumerate(y):
    ax.text(v + 3, i + .25, str(v),
            color='blue', fontweight='bold')
plt.show()
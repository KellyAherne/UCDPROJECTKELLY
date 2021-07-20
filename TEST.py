import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.25
fig = plt.subplots(figsize=(12, 8))

# set height of bar
Male = [714, 461, 813, 1104, 441]
Female = [675, 427, 803, 1108, 461]

# Set position of bar on X axis
br1 = np.arange(len(Male))
br2 = [x + barWidth for x in br1]

# Make the plot
plt.bar(br1, Male, color='r', width=barWidth,
        edgecolor='grey', label='Male')
plt.bar(br2, Female, color='g', width=barWidth,
        edgecolor='grey', label='Female')

# Adding Xticks
plt.xlabel('Categories', fontweight='bold', fontsize=15)
plt.ylabel('No. of Customers', fontweight='bold', fontsize=15)
plt.xticks([r + barWidth for r in range(len(Male))],
           ['Low', 'Quite Low', 'Mid', 'Quite High', 'High'])

plt.legend()
plt.show()
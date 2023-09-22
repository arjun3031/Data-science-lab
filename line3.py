import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 6, 18])
ypoints = np.array([6, 8, 12, 20])

plt.plot(xpoints,ypoints,'o:g', linestyle = 'dotted')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 3, 6, 18])
ypoints = np.array([3, 10, 12, 20])

plt.plot(xpoints, ypoints)
plt.title("Stop Watch Data")
plt.xlabel("Time")
plt.ylabel("Speed")
plt.show()


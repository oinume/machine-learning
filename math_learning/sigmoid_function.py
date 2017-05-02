import matplotlib.pyplot as plt
import math
import numpy as np

print(math.e)

e = math.e
dx = 0.1
x = np.arange(-8, 8, dx)

y_sig = 1 / (1 + e ** -x)

plt.plot(x, y_sig)
plt.show()

import matplotlib.pyplot as plt
import numpy as np

# 0.1刻みのリスト(0-10)
x = np.arange(0, 10, 0.1)
# print(x)

# y = 2x + 1
y = x * 2 + 1

plt.plot(x, y)
plt.show()

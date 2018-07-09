"""Softmax."""

scores = [3.0, 1.0, 0.2]

import numpy as np
import math

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    pass  # TODO: Compute and return softmax(x)
    if (type(x[0]) == list):
        j = []
        for i in x:
            divider = sum(map(lambda x: math.e ** x, [y for y in i]))
            j.append(np.mat(map(lambda x: math.e ** x / divider, [y for y in i])))
        return np.mat(j)
    else:
        divider = sum(map(lambda x: math.e ** x, [y for y in x]))
        return np.mat(map(lambda x: math.e ** x / divider, [y for y in x]))


print(softmax(scores))

# Plot softmax curves
import matplotlib.pyplot as plt
x = np.arange(-2.0, 6.0, 0.1)
# x = np.arange(2.0, 1.0, 0.1)
scores = np.vstack([x, np.ones_like(x), 0.2 * np.ones_like(x)])

plt.plot(x, softmax(scores).T, linewidth=2)
plt.show()

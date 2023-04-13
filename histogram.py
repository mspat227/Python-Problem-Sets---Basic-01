'''
26. Write a Python program to create a histogram from a given list of integers.
'''

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show() 
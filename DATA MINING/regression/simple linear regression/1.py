#imports
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#x and y  axis
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

plt.scatter(x, y, label= "stars", color= "green", marker= "o", s=30)
plt.show()

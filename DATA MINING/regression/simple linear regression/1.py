#imports
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

#defining x and y axis and reshaping to 2D Dimension so we can work with them
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

#giving names and color to x and y axis then displaying them
plt.scatter(x, y, label= "stars", color= "green", marker= "o", s=30)
#plt.show()

#fitting a linear regression means to find the function y = m*x + b
#after doing this, fx should have the mx + b
#here m is the slope and b is the intercept
fx = LinearRegression().fit(x, y) 
#I don't know what this means yet
r_sq = fx.score(x, y)

#Displaying the r_sq
print("r2:", r_sq)

#displaying the slope and the intercept using methods
print("intercept:", fx.intercept_)
print("slope:", fx. coef_)

#getting the prdiction
y_pred = fx.predict(x)
print(y_pred)
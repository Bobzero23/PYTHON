import numpy as np
from sklearn.linear_model import LinearRegression

#defining x and y axis
x = [[0, 1], [5, 1], [15, 2], [25, 5], [35, 11], [45, 15], [55, 34], [60, 35]]
y = [4, 5, 20, 14, 32, 22, 38, 43]
# setting them as array with numpy
x, y = np.array(x), np.array(y)

#train them and fitting them to fx 
fx = LinearRegression().fit(x, y)
r_sq = fx.score(x, y)

#getting the slope and the intercept
print("r2:", r_sq)
print("intercept:",fx.intercept_)
print("coefficients:", fx.coef_)
#gettign the prediction
fx_pred = fx.predict(x)
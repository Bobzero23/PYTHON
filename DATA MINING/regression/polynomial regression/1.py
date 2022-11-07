#imports
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#defining x and y axis and reshaping to 2D Dimension so we can work with them
x = np.array([5, 15, 25, 35, 45, 55]).reshape((-1, 1))
y = np.array([5, 20, 14, 32, 22, 38])

#creating a polynomial variable
transformer = PolynomialFeatures(degree=2, include_bias= False)
#fitting the polynomial x variable
transformer.fit(x)
#transforming the variable to another x variable
x_ = transformer.transform(x)

#fitting to the linear regression using new x_ and y
fx = LinearRegression().fit(x_, y)
r_sq = fx.score(x_, y)

#getting the slope and intercept
print("coefficient of determination:", r_sq)
print("intercept:",fx.intercept_)
print("coefficients:", fx.coef_)

#getting the prediction
y_pred = fx.predict(x_)
print("predicted y:", y_pred)


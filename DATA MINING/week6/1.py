
#imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from matplotlib.colors import ListedColormap

#reading the file
veri = pd.read_csv('C:\\Users\\Sony\\Documents\\BOB\\Advertising.csv')

#assigning some values
TV = veri['TV']
Radio = veri['Radio']
News = veri['Newspaper']


y = [] #for holding the y axis numbers
x = [] #for holding hte x axis numbers

#getting the length of the Tvs
#print(len(TV))

#displaying all the Tvs and Radios and Newspaper
for i in range(len(TV)):
    #print(TV[i], Radio[i], News[i])
    #adding all the Tvs and Radios to the list
    x.append([TV[i], Radio[i], News[i]])


#displaying the list
#print(x)

#creating a temporary list to hold the size of the array
temp = veri['Sales']

#adding all the element to the y axis using for loop
for i in range(len(temp)):
    y.append(temp[i])

#setting them up as array
x, y = np.array(x), np.array(y)

fx = LinearRegression().fit(x, y)
r_sq = fx.score(x, y)
print("r2:", r_sq)
print("intercept:", fx.intercept_)
print("coenfficient:",fx.coef_)

sorulan = np.array([50, 40, 30]).reshape(-1, 3)
fx_pred = fx.predict(sorulan)
print("predicted sorulan:", fx_pred)
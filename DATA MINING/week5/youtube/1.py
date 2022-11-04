#SIMPLE LINEAR REGRESSION


#imports
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

#reading the data set
df = pd.read_csv('C:\\Users\\Sony\\Documents\\BOB\\data.csv')
#displaying the data set
#print(df)

#checking if there is a null value
isNull = df.isnull().sum()
#print(isNull)

#defining the c.feature and the label
#this means all the columns excepth the charges
x = df.drop(columns= 'charges')
#print(x)

#lets take only two thing from our data set 
#because in simple linear regression only needs two variables 

#doing the split and the test
#0.4 means it will keep 40 percet for the test purpose
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size = 0.4, random_state = 0)
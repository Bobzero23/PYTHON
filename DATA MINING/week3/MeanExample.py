# The point here is to store 1000 thousands integers which are in range of 1 - 5 and find their mean
# Witht the help of some libraries we tried to some cool stuffs too like drawing tables and so on..


#imports
import random
import numpy
import pandas
import matplotlib.pyplot


#storing  1000 thousand numbers to an array
store = numpy.random.randint(1, 5, size= 10)
#to make things interesting you can play with then numbere here
#or do something like this inside the for loop
# store = numpy.random.randint(1, 5, size= j)

#displaying the 1000 numbers in array
print(store)

#finding the mean of the number we store
print(store.mean())

#Creating a list
storeList = []

#storing all the means in to the list
for i in store:
    storeList.append(store.mean())

#displaying the list
print(storeList)

#assigning data frame to a variable
dFrame = pandas.DataFrame(store)

#displaying the data frame table
print(dFrame)

#displaying the data frame graphic
dFrame.plot()
matplotlib.pyplot.show()
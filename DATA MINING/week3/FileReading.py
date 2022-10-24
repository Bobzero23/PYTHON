#Reading an excel file using python

#imports
import pandas

#Reading a file
file = pandas.read_csv('titanic.csv')
file.head() #getting the first five line of the file
file.tail() #getting the last five line of the file
file.isnull().sum() #getting the of the all null details in the file
file.groupby('sex')['age'].mean() #getting the mean by age and by sex
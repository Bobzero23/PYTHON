#Demonstration on how to find the Average of the list 

#Creating the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Finding the sum and the number of elements
counter = 0
sum = 0
for i in numbers:
    sum = sum + i
    counter = counter + 1

#Calculating the average
average = sum / counter

#Displaying the average
print("The average of the list is: ", average)
#Demonstration on how to add the numbers which are over the average to another list

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

#Displaying the average of the list
print("The average of the list is: ", average)

#Adding number over the average to the new list
over_average = []
for n in numbers:
    if n > average:
        over_average.append(n)

#Displaying the new list
print("The number over the average are: ", over_average)

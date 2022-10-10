#Demonstration on how to find the number of the elements of the list

#Creating the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Finding the number of elements
counter = 0
for i in numbers:
    counter = counter + 1

#Displaying the number of elements of the list
print("The number of elements of the list is: ", counter)
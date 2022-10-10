#Demonstration on how to find the sum of the elements of the list

#Creating the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Finding the sum
sum = 0
for i in numbers:
    sum = sum + i

#Displaying the sum
print("The sum of the elements of the list is: ", sum)
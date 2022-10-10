#Demonstration on how to find the max and the min number in the list

#Creating the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Finding the max number 
max = 0
for i in numbers:
    if i > max:
        max = i

#Displaying the max number
print("The max number is: ", max)

#Finding the min number
min = 0
for i in numbers:
    if i < min:
        min = i

#Displaying the min number
print("The min numer is: ", min)
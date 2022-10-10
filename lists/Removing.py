#Demonstration on how to remove items of the lists

#Creating a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Removing a particular item
numbers.remove(4)

#Displaying the list
print(numbers)

#Removing by index
numbers.pop(0)

#Displaying the list
print(numbers)

#Removing the last index
numbers.pop()

#Displaying the list
print(numbers)

#Another way of removing by index
del numbers[0]

#Displaying the list
print(numbers)

#Deleting the whole list
#del numbers

#Clearing the whole list
numbers.clear()

#Displaying the list
print(numbers)

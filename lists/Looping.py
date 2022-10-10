#Demonstration on how to loop through the list

#Creating a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Displaying the list
print(numbers)

#Looping the list using for
for i in numbers:
    print(i, end=", ")

print()

#Looping the list using range and len
for x in range(len(numbers)):
    print(x, end=", ")

print()

#Looping using while 
n = 0
while n < len(numbers):
    print(n, end=", ")
    n = n + 1

print()

#Another way of looping using for
[print(k, end=", ") for k in numbers]
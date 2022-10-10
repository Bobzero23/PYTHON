#Demonstration on how to deal with tuples

#Tuples are unchangeable, ordered and allow duplicates
#You can create a tuple using construcotr as in lists
#Accessing is also same as in lists
#Looping, Joining and some methods are just same

#Creating a tuple
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

#Displaying the number tuple
print(numbers)

#Getting the length of the tuple
print("The length of the tuple is: ", len(numbers))

#Creating the tuple with one item
number = (1,) #This is exactly what you should do
#number = (1) this is not a tuple this is an int
print(number) #Displaying it

#Getting the type of a tuple
print(type(numbers))

#Changing a tuple to a list
integers = list(numbers)
print(integers) #Displaying the list

#Unpacking  and Packing
#Packing is when you create a tuple and you assign the values with it
#Unpacking is when you take the values of the tuple and assignt them to the variables

#UNPACKING
phones = ("Apple", "Samsung", "Tecno")
(Best, Better, Good) = phones
print("The best phone is: ", Best)

#Use this * if the number of the varaibles are less than the number of the values
#Example *Good and the more items will be assigned to good as a list


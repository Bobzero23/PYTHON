#Demonstration on how to find the number of element of the list in the function

#Creating the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Function to find the number of elements
def number_of_elements():
    counter = 0
    for i in numbers:
        counter = counter + 1
    print("The number of element is: ", counter)

number_of_elements()
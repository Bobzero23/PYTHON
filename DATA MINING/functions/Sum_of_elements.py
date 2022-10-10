#Demonsration on how to find the sum of elements of the list 

#Creating the list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

#Function to find the sum of elements
def sum_of_elements():
    sum = 0
    for i in numbers:
        sum = sum + i
    print("The sum of elements of the list is: ", sum)

#Calling the function
sum_of_elements()
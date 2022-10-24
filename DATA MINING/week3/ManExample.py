# Finding how many random arrays make more of a man favorite film

#imports
import random
import numpy

# Creting a list for a movie
movie = []
for i in range (1, 1001):
    movie.append([random.randint(1, 5),random.randint(1, 5),random.randint(1, 5)])


# Creating an list for a man 
# Since we gonna use numpy we gonna have to use array
A = numpy.array([3, 5, 1])

#Doing the calculation and checking the coditions
count = 0
for x in movie:
    if numpy.dot(A, x) > 39:
        count = count + 1

#displaying the result
print(count)
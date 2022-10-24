# creating a random types of movies using list and array


#imports
import random

#creating an empty movie
movie = [] 

# looping 10 times 
for i in range (1,11):
    movie.append([random.randint(1, 5),random.randint(1, 5),random.randint(1, 5)])

#displaying the movie list
print(movie)
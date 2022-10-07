#Using format() method we can combine String and Integers together

a = 30
b = "I am {} years old"

#formatting Strings with Integer
print(b.format(a))

#Formatting multiple integers in String
position = 1
age = 35
year = 1987
sentence = "The {}'st winner is {} years old and was born in {}"
print(sentence.format(position, age, year))

#Indexing while formatting to make sure the arguments are in the right place
one = 1
two = 2
three = 3
counting = "let's say this is one({1}), this is two({2}) and this is three({0})"
print(counting.format(three, one, two))
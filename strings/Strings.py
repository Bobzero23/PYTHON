#assigning multiple lines of string to a variable
a = """This is how
we assign multiple lines of string
to  a single variable"""
print(a)

#In Python Strings are arrays and there is no character data type
#getting the first element of String
b = "I am going to school"
print(b[0])

#Since String are arrays we can loop through Strings using for loop
#Looping a String
c = "Loop me"
for i in c:
    print(i)

#Getting the length of a String
d = "I am too short"
print(len(d))

#Checking is a word is in a variable string (This is a boolean method)
e = "Nothing in here, leave us alone"
print("here" in e)

#Checking if 
f = "what are you looking at"
if "you" in f:
    print("Yeah it is inside it")

#Checking if Not
g = "Surely is not in here, Come on!"
if "man" not in g:
    print("Yeah it is not inside it")


#Demonstration on how to Access the list items

#Creating a list
names = ["Bob", "Kombo", "Oma", "Mido", "Mamalao", "Mamba", "Kitufe"]

#Displaying the whole list
print(names)

#Accessing the first index
print("The first index is: ", names[0])

#Accessing from the start to the third index
print(names[:3])

#Accessing frome the fifth index to the end
print(names[4:])

#Accessing 4 elements of the list from the end
print(names[-5:-1])

#Checking if a particular element is exist in the list
if "Madevu" not in names:
    print("Madevu is not in the names list..")
#Demonstration on how to change the itemes in the list

#Creating a list
names = ["Bob", "Kombo", "Oma", "Mido", "Mamalao", "Mamba", "Kitufe"]

#Displaying the list
print(names)

#Replacing "Mido" with Sadati
names[3] = "Sadati"

#Displaying the list
print(names)

#Changing the first and second element
names[0:2] = "Bobzero","KOBZY"

#Displaying the list
print(names)

#Inserting an element to a list using insert() method
names.insert(5, "Kundu")

#Displaying the list
print(names)

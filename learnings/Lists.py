list = []
list.append("mouse")
list.append("house")
list.append("blouse")

print(list)
print(len(list))
print("Index 1", list[1])

list.insert(1, "grouse")
print(list)

print("\nPrinting the list: ")
for i in range(len(list)):
    print(list[i])

del(list[1])
print("\n", list)
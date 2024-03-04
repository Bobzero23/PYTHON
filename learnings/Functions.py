def sum (a, b, c):
    return a + b + c

print(sum(1, 2, 3))

# assigning the method to a variable
mystery = sum
print(mystery(3, 4, 3))


# optional parameter
def addition (a, b, c = 0):
    return a + b + c

print(addition(1, 2))
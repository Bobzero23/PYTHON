x = 0

while x < 5:
    print(x, end=" ")
    x += 1

print()

# Starting from 0 to 10
for y in range(10):
    print(y, end=" ")

print()

# Starting from 2 to 6
# Note that 7 is not included
for y in range(2, 7):
    print(y, end=" ")

print()

# Starting from 0 to 10 increasing by 2
for y in range(0, 10, 2):
    print(y, end=" ")

print()

nums = [1, 2, 3, 4, 1]
for x in nums:
    if x == 3:
        continue
    print(x, end=" ")
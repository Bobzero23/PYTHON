m = [[1,2,3],
     [2,3,3],
     [5,4,3]]
print([list(x) for x in zip(*[x[::-1] for x in m])])
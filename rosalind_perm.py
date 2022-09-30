from permutations import permutation
import math
n = 6

data = list()
for x in range(1, n+1):
    data.append(x)
print(math.factorial(n))
for p in permutation(data):
    for x in p:
        print(x, end=" ")
    print(" ")
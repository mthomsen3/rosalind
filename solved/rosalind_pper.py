import math

# https://www.mathplanet.com/education/algebra-2/discrete-mathematics-and-probability/permutations-and-combinations

n = 98
r = 8

p = math.factorial(n) / math.factorial (n-r)

print(p % 1000000)




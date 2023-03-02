def sum_of_odd_integers(a, b):
    return sum(i for i in range(a, b+1) if i % 2 != 0)

print(sum_of_odd_integers(100, 200))

print(sum_of_odd_integers(4060, 8743))

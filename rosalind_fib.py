


# months
n = 6

# rabbit pairs
k = 1

# starting pairs
r = 1

rabbits = []

rabbits.append(1)

rabbits.append(1)

for x in range(2, n):
    rabbits.append(k * (rabbits[x-2]) + rabbits[x-1])


print(rabbits)
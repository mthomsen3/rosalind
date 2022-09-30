


n = 6
m = 3

months = n

rabbits0 = [0] * (n)
rabbits1 = [0] * (n)
rabbits2 = [0] * (n)

x = 1

rabbits0[x] = 1
rabbits1[x] = 0
rabbits2[x] = 0

x = 2

rabbits0[x] = 0
rabbits1[x] = rabbits0[x-1]
rabbits2[x] = 0

x = 3

rabbits0[x] = rabbits1[x-1] + rabbits2[x-1]
rabbits1[x] = rabbits0[x-1]
rabbits2[x] = rabbits1[x-1]

for x in range(4, n):
    rabbits0[x] = rabbits1[x-1] + rabbits2[x-1]
    rabbits1[x] = rabbits0[x-1]
    rabbits2[x] = rabbits1[x-1]


print(rabbits0)
print(rabbits1)
print(rabbits2)

print(rabbits0[n-1]+rabbits1[n-1]+rabbits2[n-1])


def fibonacci_rabbits(n, k):
    if n == 1 or n == 2:
        return 1
    else:
        return fibonacci_rabbits(n-1, k) + k*fibonacci_rabbits(n-2, k)

n, k = map(int, input().split())
print(fibonacci_rabbits(n, k))
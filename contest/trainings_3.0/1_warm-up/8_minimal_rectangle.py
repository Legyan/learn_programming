k = int(input())
mass = [float('inf'), float('inf'), -float('inf'), -float('inf')]

for x in range(k):
    x, y = [int(x) for x in input().split()]
    mass[0] = min(mass[0], x)
    mass[1] = min(mass[1], y)
    mass[2] = max(mass[2], x)
    mass[3] = max(mass[3], y)
print(*mass)

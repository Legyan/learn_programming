n = int(input())
mass = list(map(int, input().split()))
k = int(input())
res =[]
summ = 0
for i in range(k):
    summ+=mass[i]
res.append(summ/k)
for j in range(k, n):
    summ-=mass[j-k]
    summ+=mass[j]
    res.append(summ/k)
print(' '.join(map(str, res)))

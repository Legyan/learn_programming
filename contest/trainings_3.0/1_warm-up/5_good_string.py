n = int(input())
res = 0
last = int(input())
for _ in range(n - 1):
    this = int(input())
    res += min(last, this)
    last = this

print(res)

from collections import deque

n = int(input())
adj_matrix = [[int(x) for x in input().split()] for _ in range(n)]
start, end = [int(x) for x in input().split()]
dist = [-1] * n
dist[start-1] = 0
q = deque()
q.append(start-1)
while q:
    u = q.popleft()
    for v in range(n):
        if adj_matrix[u][v] and dist[v] == -1:
            q.append(v)
            dist[v] = dist[u] + 1

print(dist[end-1])

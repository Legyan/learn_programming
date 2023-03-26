def dfs(v):
    visited[v] = True
    component.append(v)
    if v in graphs:
        for neighbor in graphs[v]:
            if neighbor not in visited:
                dfs(neighbor)


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    if m == 0:
        print(1)
        print(1)
        raise SystemExit
    graphs = {}
    first = 0
    for i in range(m):
        a, b = [int(x) for x in input().split()]
        if a not in graphs:
            graphs[a] = [b]
        else:
            graphs[a].append(b)
        if b not in graphs:
            graphs[b] = [a]
        else:
            graphs[b].append(a)

    visited = {}
    component = []
    dfs(1)
    print(len(component))
    print(*sorted(component))

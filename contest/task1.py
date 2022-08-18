n = int(input())
storages = list(map(int, input().split(' ')))


def equalizer(n, storages):
    for i in range(n-1):
        if storages[i] > storages[i+1]:
            return -1
    return storages[-1] - storages[0]

print(equalizer(n, storages))

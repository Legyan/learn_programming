def find_stickers(stickers, requests):
    for p in requests:
        left = 0
        right = len(stickers) - 1
        res = 0
        while left <= right:
            pivot = (right + left) // 2
            if stickers[pivot] >= p:
                right = pivot - 1
            else:
                res = pivot + 1
                left = pivot + 1
        else:
            print(res)

if __name__ == '__main__':
    N = int(input())
    stickers_set = set()
    stickers_list = []
    all_stickers =[int(x) for x in input().split()]
    for stick in all_stickers:
        if stick not in stickers_set:
            stickers_set.add(stick)
            stickers_list.append(stick)
    K = int(input())
    collectionsts = (int(x) for x in input().split())
    stickers_list.sort()
    find_stickers(stickers_list, collectionsts)

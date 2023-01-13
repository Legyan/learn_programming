def qsort(lst):
    from random import uniform
    mid = int(uniform(0, len(lst)))
    low = []
    high = []
    if len(lst) < 2:
        return lst
    for i in range(len(lst)):
        if i != mid:
            if lst[mid] < lst[i]:
                high.append(lst[i])
            else:
                low.append(lst[i])
    low = qsort(low)
    low.append(lst[mid])
    return low + qsort(high)


if __name__ == '__main__':
    from random import shuffle
    lst = list(range(0, 100, 1))
    shuffle(lst)
    print(qsort(lst))

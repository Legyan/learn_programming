def twoSum(N, lst):
    for i in range(N):
        for j in range(i+1, N):
            if lst[i] + lst[j] == x:
                return ' '.join(map(str, (lst[i], lst[j])))
    else:
        return None


def twoSum_2_point(X, lst):
    low = 0
    high = len(lst) - 1
    while low < high:
        summ = lst[low] + lst[high]
        if summ == X:
            l1, l2 = str(lst[low]), str(lst[high])
            return ' '.join((l1, l2))
        elif summ > X:
            high -= 1
        else:
            low += 1
    else:
        return None


if __name__ == '__main__':
    n = 6
    lst = [1, 3, 5, 6, 8, 9]
    x = 11
    print(twoSum(n, lst))
    print(twoSum_2_point(x, lst))

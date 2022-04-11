def search(list: list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low + high) // 2
        if list[mid] == item:
            return mid
        elif list[mid] < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


if __name__ == '__main__':
    lst = list(range(0, 100, 2))
    print(search(lst, 33))
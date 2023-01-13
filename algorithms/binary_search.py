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


def search_rec(list, item):
    low = 0
    high = len(list) - 1
    mid = (low + high) // 2
    if list[mid] == item:
        return mid
    elif list[mid] < item:
        try:
            return mid + 1 + search_rec(list[mid+1:], item)
        except Exception:
            return None
    else:
        try:
            return search_rec(list[:mid-1], item)
        except Exception:
            return None


if __name__ == '__main__':
    lst = list(range(0, 100, 1))
    print(search(lst, 32))
    print(search_rec(lst, 44))

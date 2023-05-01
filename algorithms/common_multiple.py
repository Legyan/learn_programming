def cm(a, b):
    """
    Возвращает общий делитель двух чисел
    """
    x = a % b
    if x == 0:
        return b
    else:
        return cm(b, x)


if __name__ == '__main__':
    print(cm(12, 16))

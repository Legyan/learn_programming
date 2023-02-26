def test_work(n, k, line, variant):
    pos1 = (line - 1) * 2 + variant - k
    pos2 = (line - 1) * 2 + variant + k
    line1 = (pos1 + 1) // 2
    line2 = (pos2 + 1) // 2
    if pos1 > 0 and (pos2 > n or abs(line - line1) < abs(line - line2)):
        return ' '.join((str(line1), str(2 - pos1 % 2)))
    elif pos2 <= n:
        return ' '.join((str(line2), str(2 - pos2 % 2)))
    else:
        return -1

if __name__ == '__main__':
    n = int(input())
    k = int(input())
    line = int(input())
    variant = int(input())
    print(test_work(n, k, line, variant))

def isPalindrome(x: int) -> bool:
    strx = str(x)
    i = 0
    while i < len(strx):
        if strx[i] != strx[-i-1]:
            return False
        i += 1
    return True


if __name__ == '__main__':
    x = isPalindrome(123)
    y = isPalindrome(121)
    print(x, y)

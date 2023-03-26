def repetition_of_letters(s):
    res = [0] * 26
    len_s = len(s)
    for i in range(len_s):
        res[ord(s[i]) - ord('a')] += (i + 1) * (len_s - i)
    for i in range(26):
        if res[i]:
            print(f'{chr(ord("a")+i)}: {res[i]}')


if __name__ == '__main__':
    s = input()
    repetition_of_letters(s)

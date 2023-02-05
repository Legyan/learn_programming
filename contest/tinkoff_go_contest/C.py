def main():
    block_1 = int(input())
    symbols_1 = [int(x) for x in input().split()]
    numbers_1 = [int(x) for x in input().split()]
    block_2 = int(input())
    symbols_2 = [int(x) for x in input().split()]
    numbers_2 = [int(x) for x in input().split()]
    list_1 = []
    list_2 = []
    for i in range(block_1):
        list_1.extend([symbols_1[i]] * numbers_1[i])
    for i in range(block_2):
        list_2.extend([symbols_2[i]] * numbers_2[i])
    result = 0
    for i in range(len(list_1)):
        if list_1[i] != list_2[i]:
            result += i + 1
    print(result)


if __name__ == '__main__':
    main()

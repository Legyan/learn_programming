# ID 79393055
def main():
    k = int(input())
    numbers = []
    for i in range(4):
        for x in input():
            try:
                numbers.append(int(x))
            except ValueError:
                pass

    set_of_nums = set(numbers)
    max_score = 0
    sum_k = 2 * k
    for x in set_of_nums:
        if numbers.count(x) <= sum_k:
            max_score += 1
    print(max_score)

if __name__ == '__main__':
    main()

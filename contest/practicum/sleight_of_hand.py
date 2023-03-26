# ID 79424704
def get_input():
    k = int(input())
    numbers = []
    for i in range(4):
        for x in input():
            try:
                numbers.append(int(x))
            except ValueError:
                pass
    return k, numbers


def max_score(k, numbers):
    set_of_nums = set(numbers)
    max_score = 0
    sum_k = 2 * k
    for x in set_of_nums:
        if numbers.count(x) <= sum_k:
            max_score += 1
    return max_score


def main():
    print(max_score(*get_input()))


if __name__ == '__main__':
    main()

def main():
    n = int(input())
    k = int(input())
    if n != k:
        max_sheepfoals = (n - (k - 1)) ** 2 + (k - 1)
        if n % k == 0:
            min_sheepfoals = int(k * (n / k) ** 2)
        else:
            big_sheepfoal = round(n / k)
            small_sheepfoal = big_sheepfoal - 1
            number_of_big = 0
            number_of_small = k
            remainder = n
            while remainder/number_of_small > big_sheepfoal - 1:
                number_of_big += 1
                remainder -= big_sheepfoal
                number_of_small -= 1
            min_sheepfoals = (number_of_big * (big_sheepfoal ** 2) +
                              number_of_small * (small_sheepfoal ** 2))
    else:
        max_sheepfoals = min_sheepfoals = k
    print(min_sheepfoals, max_sheepfoals)


if __name__ == '__main__':
    main()

num = int(input())


def factorization(num):
    factors = []
    divisor = 2
    while pow(divisor, 2) <= num:
        if num % divisor == 0:
            factors.append(divisor)
            num = num / divisor
        else:
            divisor += 1
    else:
        factors.append(int(num))
    return ' '.join([str(x) for x in factors])


print(factorization(num))

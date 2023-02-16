def sync_time(A, B, C):
    A = [int(x) for x in A.split(':')]
    B = [int(x) for x in B.split(':')]
    C = [int(x) for x in C.split(':')]
    As = A[0] * 60 * 60 + A[1] * 60 + A[2]
    Bs = B[0] * 60 * 60 + B[1] * 60 + B[2]
    Cs = C[0] * 60 * 60 + C[1] * 60 + C[2]
    if Cs < As:
        if A[2] % 2 == C[2] % 2:
            delta = int((24 * 60 * 60 - As + Cs) // 2)
        else:
            delta = int((24 * 60 * 60 - As + Cs) // 2 + 1)
    else:
        if A[2] % 2 == C[2] % 2:
            delta = int((Cs - As) // 2)
        else:
            delta = int((Cs - As) // 2 + 1)
    res_s = Bs + delta
    if res_s > 24 * 60 * 60:
        res_s -= 24 * 60 * 60
    res_hour = res_s // (60 * 60)
    res_minute = (res_s - res_hour * 60 * 60) // 60
    res_second = (res_s - res_hour * 60 * 60) % 60
    results = [res_hour, res_minute, res_second]
    for i in range(3):
        if results[i] < 10:
            results[i] = '0' + str(results[i])
        else:
            results[i] = str(results[i])
    return ':'.join(results)


if __name__ == '__main__':
    A = input()
    B = input()
    C = input()
    print(sync_time(A,B,C))
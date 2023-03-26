def oper_sys(N, M):
    if not M or not N:
        return 0
    seg_set = set()
    for i in range(1, N + 1):
        seg_start, seg_stop = [int(x) for x in input().split()]
        segs_to_remove = []
        for seg in seg_set:
            if seg_start <= seg[1] and seg_stop >= seg[0]:
                segs_to_remove.append(seg)
        for seg1 in segs_to_remove:
            seg_set.remove(seg1)
        seg_set.add((seg_start, seg_stop))
    return len(seg_set)


if __name__ == '__main__':
    m = int(input())
    n = int(input())
    print(oper_sys(n, m))

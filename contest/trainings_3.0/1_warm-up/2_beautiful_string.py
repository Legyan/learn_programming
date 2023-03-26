def beautify_string(s, k):
    left = 0
    counts = {}
    max_count = 0
    max_beauty = 0
    for right in range(len(s)):
        if s[right] not in counts:
            counts[s[right]] = 0
        counts[s[right]] += 1
        max_count = max(max_count, counts[s[right]])
        if right - left + 1 - max_count > k:
            counts[s[left]] -= 1
            left += 1
        max_beauty = max(max_beauty, right - left + 1)
    return max_beauty


if __name__ == '__main__':
    k = int(input())
    s = input()
    print(beautify_string(s, k))

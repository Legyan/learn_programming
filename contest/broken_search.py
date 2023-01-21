def broken_search(nums, target) -> int:
    if target == nums[-1]:
        return len(nums) - 1
    first = nums[0]
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    guess = nums[mid]
    while guess != target:
        if low == high:
            return -1
        elif first > target > guess \
                or first < guess < target \
                or target < first < guess:
            low = mid + 1
            mid = low + (high - low) // 2
            guess = nums[mid]
        elif target < guess or guess < first:
            high = mid
            mid = low + (high - low) // 2
            guess = nums[mid]
        else:
            return -1
    return mid

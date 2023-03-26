# ID 81408032
from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Поиск элемента в сломанном списке и возвращение его индекса"""
    validate_input(nums, target)
    if target == nums[-1]:
        return len(nums) - 1
    first = nums[0]
    low = 0
    high = len(nums) - 1
    mid = (low + high) // 2
    guess = nums[mid]
    try:
        while guess != target:
            if low == high:
                return -1
            elif (target > guess > first
                  or first > target > guess
                  or guess > first > target):
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
    except TypeError:
        raise ValueError(
            'The nums in list must be integer'
        )


def validate_input(nums: List[int], target: int) -> None:
    """Валидация входных данных"""
    if not isinstance(nums, list):
        raise TypeError(
            'The nums must be list'
        )
    if len(nums) > 10000:
        raise ValueError(
            'The number of nums must be less than 10_000'
        )
    if not isinstance(target, int) or target < 0:
        raise ValueError(
            'The target must be positive integer'
        )

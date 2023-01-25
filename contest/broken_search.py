from typing import List


def broken_search(nums: List[int], target: int) -> int:
    """Поиск элемента в сломанном списке и возвращение его индекса"""
    # validate_input(nums, target)
    # Если проводить валидацию каждого числа в списке,
    # то невозможно обеспечить скорость работы программы
    # за O(log n). При проведении полной валидации данных
    # программа не укладывается в 1.5 секунды.
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
    for num in nums:
        if not isinstance(num, int) or not 0 <= num <= 1000000:
            # По условию задачи число в списке не может превышать 10 000,
            # но с таким условием не проходится тест №37,
            # где одно из чисел 122222.
            raise ValueError(
                'The num must be integer '
                'in the range from 0 to 10_000'
            )

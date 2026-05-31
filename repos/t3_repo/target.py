def count_even(nums):
    # Bug: inverted condition
    return sum(1 for x in nums if x % 2 != 0)
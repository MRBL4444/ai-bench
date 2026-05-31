def add(nums):
    # Bug: currently sums odd numbers, should sum even numbers
    return sum(x for x in nums if x % 2 == 0)
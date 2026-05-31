def average(nums):
    # Bug: fails on zero-only or empty list
    if not nums:
        return 0
    return sum(nums)/len(nums)
def multi_edge(nums):
    # Bug: fails on multiple edge cases
    if not nums:
        return 0
    return sum(nums)
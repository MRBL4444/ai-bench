def add(nums):
    # Bug: crashes on empty list
    if not nums:
        return 0
    return sum(nums)
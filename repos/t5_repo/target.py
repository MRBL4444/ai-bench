def nested_sum(matrix):
    # Bug: resets accumulator in nested loop
    total = 0
    for row in matrix:
        row_sum = 0
        for val in row:
            row_sum += val
        total += row_sum
    return total
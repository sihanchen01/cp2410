def count_ones(A:list[list[int]]) -> int:
    """ Return number of 1s in the matrix(n x n). """
    result = 0
    for row in A:
        result += count_ones_in_row(row)

    return result

def count_ones_in_row(row:list[int]) -> int:
    """ Return number of one in a row. """
    n = len(row)

    if n == 1:
        return 1 if row[0] == 1 else 0

    left = row[:n//2]
    right = row[n//2:]
    if left[-1] == 0 or right[0] == 1:
        if left[-1] == 0:
            return count_ones_in_row(left)
        else: # 1 in right 
            return len(left) + count_ones_in_row(right)
    else:
        return len(left)
    
A = [[1, 1, 1, 1, 1], [1, 1, 1, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 0]]
print(count_ones(A))

def in_place_sort(A: list[int]) -> list:
    """ Sort all 0s before 1s in place. """
    i, j = 0, len(A) - 1
    # from left to right, find first 1 at index i
    for i in range(len(A)):
        if A[i] == 1:
            break
    # from right to left, find first 0 at index j
    for j in range(len(A)-1, -1, -1):
        if A[j] == 0:
            break
    # if i and j meet, the list is sorted
    if i > j:
        return A
    else:
        # swap i, j
        A[i] = 0
        A[j] = 1
        return in_place_sort(A)

A = [1, 0, 1, 0, 1, 1, 0]
print(in_place_sort(A))
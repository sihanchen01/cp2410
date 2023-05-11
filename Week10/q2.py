def get_non_duplicates(A: list) -> list:
    """ Return all non-duplicated elements. """
    result = []
    # In case of empty list
    if not A:
        return result
    # Insert the first element, start iteration from index of 1
    result.append(A[0])
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            result.append(A[i])
    return result

A = [0, 1, 1, 2, 3, 5, 8]
print(get_non_duplicates(A))
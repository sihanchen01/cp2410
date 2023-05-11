def find_winner(S:list[int]) -> int:
    """ Return the most frequent int, which represents a candidate. """
    # two edge cases
    if not S:
        return -1
    if len(S) == 1:
        return S[0]

    merge_sort(S)
    print(S)
    winner = S[0]
    prev_start = 0
    most_frequent = 0
    for i in range(1, len(S)):
        if S[i] != S[i-1]:
            count = i - prev_start
            if count > most_frequent:
                most_frequent = count
                winner = S[i-1]
            prev_start = i
    return (winner, most_frequent)




def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j] 
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

S = [1, 2, 1, 2, 0, 5, 2, 3, 5, 1, 2]
print(find_winner(S))
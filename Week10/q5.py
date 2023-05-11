def find_election_winner(S: list[str]) -> str:
    """ Find the ecandidate with most votes. """
    d = {}
    for i in S:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 0
    
    # return the key with highest value
    return max(d, key=d.get)
    
S=['a', 'a', 'b', 'c', 'c', 'b', 'b']
print(find_election_winner(S))
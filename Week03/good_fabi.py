def good_fabi(n):
    if n <= 2:
        return (n, 1)
    else:
        (a,b) = good_fabi(n - 1)
        return (a+b, a)

for i in range(5, 10):
    print(f"fabi till {i}: {good_fabi(i)}")

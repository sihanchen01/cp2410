test = [4, 2, 7, 1, 8, 5]


def insertion_sort(l):
    n = len(l)
    for i in range(n):
        pos = i
        value = l[i]
        while pos > 0 and l[pos - 1] > value:
            l[pos] = l[pos - 1]
            pos -= 1
        l[pos] = value

    print(l)



if __name__ == "__main__":
    print(test)
    insertion_sort(test)

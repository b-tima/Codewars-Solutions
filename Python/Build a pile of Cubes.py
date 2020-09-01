def find_nb(m):
    n = 0
    sum = 0
    while sum < m:
        n += 1
        sum += pow(n, 3)
    if sum == m:
        return n
    return -1
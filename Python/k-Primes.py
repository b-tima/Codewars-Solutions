from math import sqrt

cache = {}

def dividors(n):
    if n in cache:
        return cache[n]
    for i in range(2, int(sqrt(n))+1):
        if n % i == 0:
            cache[n] = dividors(n/i) + 1
            return cache[n]
    return 1

def count_Kprimes(k, start, nd):
    res = []
    for i in range(start, nd+1):
        if dividors(i) == k:
            res.append(i)
    return res

def puzzle(s):
    ones = count_Kprimes(1, 2, s)
    threes = count_Kprimes(3, 2, s-ones[0])
    sevens = count_Kprimes(7, 2, s-threes[0]-ones[0])
    k = 0
    while len(ones) > 0:
        candidate = ones.pop()
        k += len([True for x in threes for y in sevens if x + y + candidate == s])
    return k
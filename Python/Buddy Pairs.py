def s(n):
    prime_dividors = {}
    t = n
    d = 2;
    sum_of_primes = 1
    while d*d <= t:
        if t % d == 0:
            prime_dividors[d] = prime_dividors[d] + 1 if d in prime_dividors else 1
            t /= d
            d = 2
            continue
        d+=1
    prime_dividors[t] = prime_dividors[t] + 1 if t in prime_dividors else 1
    for p in prime_dividors:
        temp = 0
        for i in range(0, prime_dividors[p]+1):
            temp += pow(p, i)
        sum_of_primes *= temp
    return sum_of_primes - n

def buddy(start, limit):
    for n in range(start, limit):
        m = s(n) - 1
        if m < start:
            continue
        if s(m) - 1 == n:
            return [n, m]
    return "Nothing"

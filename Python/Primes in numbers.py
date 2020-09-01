def primeFactors(n):
    factors = []
    found_all = False
    while not found_all:
        found_all = True
        for num in range(2, int(n)):
            if (n/num).is_integer():
               n /= num
               factors.append(num)
               found_all = False
               break
    factors.append(int(n))
    factSet = set(factors)
    result = ""
    for fact in sorted(factSet):
        result += "({}{})".format(fact, "**" + str(factors.count(fact)) if factors.count(fact) > 1 else "")
    return result
cache = {}

def fibonacci(n):
    if n in [0, 1]:
        return n
    if n in cache:
        return cache[n]
    cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]
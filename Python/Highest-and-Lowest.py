def high_and_low(numbers):
    return "{} {}".format(max(int(c) for c in numbers.split()), min(int(c) for c in numbers.split()))
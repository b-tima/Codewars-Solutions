def digital_root(n):
    return n if len(n) == 1 else digital_root(sum(int(n) for n in str(n)))
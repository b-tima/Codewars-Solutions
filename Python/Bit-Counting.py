def count_bits(n):
    return sum(int(i) for i in '{0:08b}'.format(n))
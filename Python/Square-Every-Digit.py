def square_digits(num):
    return int("".join(str(int(i)*int(i)) for i in str(num)))
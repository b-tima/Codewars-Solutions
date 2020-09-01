def narcissistic( value ):
    sum = 0
    for character in str(value):
        sum += pow(int(character), len(str(value)))
    if sum == value:
        return True
    return False
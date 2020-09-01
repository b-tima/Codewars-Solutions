grid = ["abcde123", "fghij456", "klmno789", "pqrst.@0", "uvwxyz_/", "% "]

def tv_remote(word):
    steps = 0
    pos = (0, 0)
    lastUpper = False
    for c in word:
        index = (0, 0)
        print(word)
        if c.isalpha() and c.isupper() != lastUpper:
            steps += abs(5 - pos[0]) + abs(0 - pos[1]) + 1
            pos = (5, 0)
            index = next((grid.index(x), x.index(c.lower())) for x in grid if c.lower() in x)
        elif c == ' ':
            steps += abs(5 - pos[0]) + abs(1 - pos[1]) + 1
            pos = (5, 1)
            continue
        else:
            index = next((grid.index(x), x.index(c.lower())) for x in grid if c.lower() in x)
        steps += abs(index[0] - pos[0]) + abs(index[1] - pos[1]) + 1
        pos = index
        if c.isalpha():
            lastUpper = c.isupper()
            
    return steps
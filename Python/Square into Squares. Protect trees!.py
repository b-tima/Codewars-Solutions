# https://stackoverflow.com/questions/54079405/kata-problem-square-into-squares-protect-trees
def decompose(n):
    goal = 0
    result = [n]

    while result:
        current = result.pop()

        goal += current**2
        for x in range(current - 1, 0, -1):
            if goal - (x**2) >= 0:
                goal -= x**2
                result.append(x)
            if goal == 0:
                result.sort()
                return result
    return None
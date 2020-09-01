def validBraces(string):
    counter = {')': '(', ']': '[', '}': '{'}
    braces = []
    for c in string:
        if c in "([{":
            braces.append(c)
        elif len(braces) == 0 or counter[c] != braces.pop():
            return False
    return len(braces) == 0
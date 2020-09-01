from math import ceil, sqrt

def code(s):
    n = ceil(sqrt(len(s.replace('\n', ''))))
    s += "".join(chr(11) for i in range(n*n-len(s.replace('\n', ''))))
    code = ""
    for i in range(n):
        code += "".join(s[i + n*j] for j in range(n-1, -1, -1)) + ("\n" if i != n - 1 else '')
    return code

def decode(s):
    n = int(sqrt(len(s)))
    s = s.replace('\n', '')
    code = ""
    for i in range(n-1, -1, -1):
        code += "".join(s[i + n*j] for j in range(n))
    return code.replace(chr(11), '')
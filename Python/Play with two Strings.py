def work_on_strings(a,b):
    def mapChar(s1, s2):
        return map(lambda x: x.swapcase() if s1.lower().count(x.lower()) % 2 == 1 else x, s2)
    return "".join(mapChar(b, a)) + "".join(mapChar(a, b))
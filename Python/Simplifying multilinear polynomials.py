def nextTerm(poly, index):
    if index >= len(poly):
        return (None, None)
    num = 1 if poly[index] == '+' or (index == 0 and poly[index] != '-') else -1
    res = ""
    if index > 0 or (index == 0 and num < 0):
        index += 1
    while index < len(poly) and poly[index] not in "+-":
        if poly[index].isnumeric():
            num = num*10 if num < 10 else num
            num = (num/abs(num))*int(poly[index])
        else:
            res += poly[index]
        index += 1
    return (("".join(sorted(res)), int(num)), index)

def simplify(poly):
    terms = {}
    if poly[0] == '+':
        poly = poly[1:]
    term, index = nextTerm(poly, 0)
    while term != None:
        terms[term[0]] = terms[term[0]] + term[1] if term[0] in terms else term[1]    
        term, index = nextTerm(poly, index)
    expression = "".join("{}{}".format(     "+{}".format(terms[k]) if terms[k] > \
                                            1 else terms[k] if abs(terms[k]) > 1 \
                                            else ('+' if terms[k] > 0 else '-'), k)\
                                            for k in sorted(terms, key=lambda x: (len(x), \
                                            x, terms[x])) if terms[k] != 0)
    return expression if expression[0] != '+' else expression[1:]
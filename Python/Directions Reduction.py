def dirReduc(arr):
    res = []
    pairs = {frozenset(["NORTH", "SOUTH"]), frozenset(["EAST", "WEST"])}
    for dir in arr:
        last = res[len(res)-1] if len(res) > 0 else ""
        if {dir, last} in pairs:
            res.pop()
        else:
            res.append(dir)
    return res
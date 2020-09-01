from math import floor
def race(v1, v2, g):
    if v1 >= v2: return None
    t = floor(3600*g/(v2-v1))
    h, t = divmod(t, 3600)
    m, t = divmod(t, 60)
    return [h, m, t]
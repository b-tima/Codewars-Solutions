from math import pow

def calculate_1RM(w, r):
    if r == 0:
        return 0
    if r == 1:
        return w
    
    epley = w * (1 + r / 30)
    mcgotlin = 100 * w / (101.3 - 2.67123 * r)
    lombardi = w * pow(r, 0.1)

    return round(max([epley, mcgotlin, lombardi]))
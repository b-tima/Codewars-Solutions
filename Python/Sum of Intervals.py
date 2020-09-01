def sum_of_intervals(intervals):
    def overlap(I1, I2):
        return I1[0] < I2[1] and I2[0] < I1[1]

    def combine(I1, I2):
        a = I1[0]
        b = I1[1]
        c = I2[0]
        d = I2[1]

        if c <= a and d >= b:
            return I2
        if a <= c and b >= d:
            return I1
        
        if c >= a and b <= d:
            return (a, d)
        if a >= c and b >= d:
            return (c, b)

    change = True
    while change:
        change = False
        for i, I1 in enumerate(intervals):
            for j, I2 in enumerate(intervals):
                if i != j and overlap(I1, I2):
                    intervals.remove(I1)
                    intervals.remove(I2)
                    intervals.append(combine(I1, I2))
                    change = True
                    break
            if change:
                break

    size = 0
    for inter in intervals:
        size += abs(inter[1] - inter[0])        
    return size
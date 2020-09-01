class Time:
    def __init__(self, scale, t):
        self.scale = scale
        self.t = t
    
    def getScale(self):
        return self.scale if self.t == 1 else self.scale + "s"

def format_duration(seconds):
    if seconds == 0:
        return "now"
    
    years, seconds = divmod(seconds, 60*60*24*365)
    days, seconds = divmod(seconds, 60*60*24)
    hours, seconds = divmod(seconds, 60*60)
    minutes, seconds = divmod(seconds, 60)

    times = [Time("year", years), Time("day", days), Time("hour", hours), Time("minute", minutes), Time("second", seconds)]
    remainder = []

    for time in times:
        if time.t == 0:
            continue
        else:
            remainder.append(time)
    
    first = False
    second = False

    for time in remainder[::-1]:
        temp = "{} {}".format(time.t, time.getScale())
        if not first:
            result = temp
            first = True
            continue
        if not second:
            result = temp + " and " + result
            second = True
            continue
        result = temp + ", " + result
    
    return result
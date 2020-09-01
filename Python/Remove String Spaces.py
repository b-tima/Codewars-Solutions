def no_space(x):
    returnVal = ""
    currentStr = ""
    for i in x:
        if(i == " "):
            returnVal += currentStr
            currentStr = ""
        else:
            currentStr += i
    return returnVal + currentStr
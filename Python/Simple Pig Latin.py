def pig_it(text):
    words = text.split(' ')
    result = ""
    for word in words:
        if word in ['.', ',', '!', '?']:
            result += word + " "
            continue
        cap = word[0]
        rem = word[1:len(word)]
        result += "{}{}ay ".format(rem, cap)
    return result.strip()
def spin_words(sentence):
    res = ""
    for word in sentence.split():
        if len(word) < 5:
            res += word + " "
        else:
            res += word[::-1] + " "
    return res[0:-1]

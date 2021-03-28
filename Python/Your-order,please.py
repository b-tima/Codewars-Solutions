def order(sentence):
    splitted = sentence.split()
    wordsInOrder = ['']*len(splitted)
    for word in splitted:
        for c in word:
            if c.isnumeric():
                wordsInOrder[int(c) - 1] = word
                break
    return " ".join(wordsInOrder)
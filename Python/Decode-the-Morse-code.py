def firstWord(string):
    i = 0
    result = ""
    while string[i] != ' ':
        result += string[i]
        i += 1
        if i > len(string) - 1:
            return result
    return ' ' if i == 0 else result

def decodeMorse(morse_code):
    morse_code = morse_code.strip()
    result = ""
    while len(morse_code) > 0:
        word = firstWord(morse_code)
        morse_code = morse_code[len(word)+1:]
        if word == " ":
            result += " "
        else:
            result += MORSE_CODE[word]
            
    return result

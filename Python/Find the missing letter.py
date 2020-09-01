def find_missing_letter(chars):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(alphabet.find(chars[0]), len(alphabet)):
        if alphabet[i] != chars[0]:
            return alphabet[i]
        chars = chars[1:len(chars)]
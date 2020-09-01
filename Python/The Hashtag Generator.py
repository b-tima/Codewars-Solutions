def generate_hashtag(s):
    if len(s.replace(' ', '')) == 0 or len(s.replace(' ', '')) > 140:
        return False
    splitted = s.strip().split(' ')
    result = ""
    for word in splitted:
        result += word.capitalize()
    return '#' + result
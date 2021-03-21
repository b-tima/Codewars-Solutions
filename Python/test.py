from time import sleep

def index_of(words, target):
    middle = len(words) // 2
    width = middle
    while words[middle] != target:
        sleep(1)
        print(words[middle])
        print(middle)
        print(width)
        # Does index and target have the same number of letters?
        if len(words[middle]) < len(target):
            width = width // 2
            middle = middle + width
            continue
        elif len(words[middle]) > len(target):
            width = width // 2
            middle = middle // 2
            continue

        num_upper_middle = sum(1 for c in words[middle] if c.isupper())
        num_upper_target = sum(1 for c in target if c.isupper())
        
        if num_upper_middle > num_upper_target:
            width  = width // 2
            middle = middle + width
            continue
        elif num_upper_middle < num_upper_target:
            width = width // 2
            middle = middle // 2
            continue

        if words[middle] < target:
            width  = width // 2
            middle = middle + width
        else:
            width = width // 2
            middle = middle // 2
        
    return middle

index = index_of(['JaCk', 'Jack', 'jack', 'jackk', 'COdewars', 'codeWars', 'abcdefgh', 'codewars', 'codewarsss'], 'codewars')
print(index)
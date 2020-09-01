def parse_int(string):
    dictionary = {  "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
                    "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
                    "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
                    "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50,
                    "sixty": 60, "seventy": 70, "eighty": 80, "ninety": 90}
    scalers = {"hundred": 100, "thousand": 1000, "million": 1000000}

    words = string.split(' ')

    number = 0
    index = 0
    current_number = 0
    current_scale = 0

    prev_scaler = 0

    while index < len(words):
        if words[index] == "and":
            index += 1
            continue
        
        if words[index] in scalers:
            if scalers[words[index]] < prev_scaler:
                number += current_number
                current_number = current_scale*scalers[words[index]]
            else:
                current_number = (current_number + current_scale)*scalers[words[index]]
            current_scale = 0
            prev_scaler = scalers[words[index]]
        else:
            seperated = words[index].split('-')
            for num in seperated:
                current_scale += dictionary[num]
        index+=1
                
    return number + current_number + current_scale
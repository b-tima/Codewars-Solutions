def solution(number):
    roman_numerals = "IVXLCDM"
    roman_numerals_value = [1, 5, 10, 50, 100, 500, 1000]
    sum = 0;
    numerals = [c for c in number]

    while len(numerals) > 0:
        current_numeral = numerals[0]
        numeral_position = roman_numerals.index(current_numeral)
        # Peek next numeral
        if len(numerals) > 1:
            peek_numeral = numerals[1]
            peek_position = roman_numerals.index(peek_numeral)
            for i in range(current_numeral, peek_position + 1):
                

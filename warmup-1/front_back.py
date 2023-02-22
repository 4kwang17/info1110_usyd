def front_back(str):
    # letter with only one character or no character is unchanged
    if len(str) <= 1:
        answer = str
        return answer

    first_char = str[0]
    last_char = str[-1]

    # slicing out the first & last char for middle_char
    middle_char = str[:-1]
    middle_char = middle_char[1:]

    # exchange first and last chars by concatenation
    answer = last_char + middle_char + first_char

    return answer
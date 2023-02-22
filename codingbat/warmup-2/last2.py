def last2(str):
    # initialise answer variable as 0
    answer = 0

    # if the length of the string > 2
    if len(str) > 2:
        # string of last 2 characters of the string
        last = str[-2:]

        # iterate from the beginning of the string to the second last character
        for i in range(0, len(str) - 1):
            # if two consecative characters matches with last 2 characters of the string
            if str[i] + str[i+1] == last:
                # count up by 1
                answer += 1

        # minus 1 for excluding the end substring
        answer -= 1

        return answer

    # else where length of string is < 2 there is no repetition, returns 0
    else:
        return answer
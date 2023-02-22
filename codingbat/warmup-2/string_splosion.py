def string_splosion(str):
    answer = ""

    for i in range(0, len(str)):
        answer += str[:i+1]
    
    return answer
def string_match(a, b):
    # set length equal to shorter length of two string
    if len(a) < len(b):
        length = len(a)
    else:
        length = len(b)

    count = 0

    for i in range(0, length - 1):
        if a[i] + a[i + 1] == b[i] + b[i + 1]:
            count += 1
    
    return count

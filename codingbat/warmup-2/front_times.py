def front_times(str, n):
    str_len = len(str)
    if str_len < 3:
        return str * n
    else:
        return str[:3] * n
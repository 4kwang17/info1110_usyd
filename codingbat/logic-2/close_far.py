def close_far(a, b, c):
    num_close = 0
    if abs(a - b) <= 1: num_close += 1
    if abs(b - c) <= 1: num_close += 1
    if abs(c - a) <= 1: num_close += 1
    if num_close == 1: return True
    else: return False
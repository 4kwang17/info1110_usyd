def pos_neg(a, b, negative):
    if not negative:
        if a * b > 0:
            return False
        else:
            return True
    elif negative:
        if a < 0 and b < 0:
            return True
        else:
            return False
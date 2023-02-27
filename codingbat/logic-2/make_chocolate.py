def make_chocolate(small, big, goal):
    for i in range(goal, goal - small - 1, -1):
        if i % 5 == 0 and i // 5 <= big:
            return goal - i
    return -1
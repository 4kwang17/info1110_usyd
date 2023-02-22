def rotate_left3(nums):
    answer = nums
    left = answer.pop(0)
    answer.append(left)
    return answer
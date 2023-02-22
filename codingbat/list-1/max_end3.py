def max_end3(nums):
    if nums[0] > nums[-1]:
        larger = nums[0]
    else:
        larger = nums[-1] 

    return [larger]*3
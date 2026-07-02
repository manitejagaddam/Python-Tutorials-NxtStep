nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''

    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 = 55
    
    55 / 10 -> 5.5

'''


def average(nums):
    average_val = 0
    # logic
    sum_val = 0
    n = len(nums)
    for idx in range(n):
        sum_val = sum_val + nums[idx]
    
    print(f"Sum val -> {sum_val}")
    
    average_val = sum_val / n    
    return average_val

print(average(nums)) # 5.5
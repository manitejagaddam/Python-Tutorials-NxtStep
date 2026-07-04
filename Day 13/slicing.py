'''
Slicing
    1. dividing into thin parts
    2. dividing into multiple parts
'''


# nums = [1, 2, 3, 4, 5, 6, 7, 8]

# nums1 = nums[3:]


# print(nums1)



# Negative Indexes
    #   [0,  1,  2,  3,  4,  5,  6,  7]
nums =  [1,  2,  3,  4,  5,  6,  7,  8]
    #  [-8, -7, -6, -5, -4, -3, -2, -1]


n = len(nums)

# for idx in range(0, n, 1):
#     # print(idx)
#     print(nums[idx])


for idx in range(-1,-n -1,-1):
    print(nums[idx])

# print(nums[-2])



# print the list (1, 2, 3, 4, 5, 6, 7, 8) using negative indexes
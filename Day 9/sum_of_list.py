nums = [10, 20, 30, 40, 50, 60]

# print the sum of the above list ==> 210

# print(210)

n = len(nums)

sum_val = 0

for idx in range(0, n):
    # print(nums[idx])
    sum_val = sum_val + nums[idx]

print(sum_val)
nums = [10, 20, 30, 40, 50]

print(nums[0])
print(nums[1])
print(nums[2])
print(nums[3])

n = len(nums) # 4

sum_val = 0

for idx in range(n): # 0 1 2 3
    print(nums[idx])
    sum_val = sum_val + nums[idx]


print(sum_val)


def sum_list(nums):
    sum_val = 0
    n = len(nums)
    for idx in range(n):
        sum_val = sum_val + nums[idx]
        
    return sum_val

print(sum_list(nums))
nums = [1,2,3,44,5,6,7,8,9,10]

max_ele = float('-inf')

n = len(nums)

for idx in range(n):
    if nums[idx] > max_ele :
        max_ele = nums[idx]

sec_large_ele = float('-inf')

for idx in range(n):
    if nums[idx] > sec_large_ele and nums[idx] < max_ele:
        
        sec_large_ele = nums[idx]


    print(f"Number : {nums[idx]}, max_ele : {max_ele}, second maximum ele : {sec_large_ele}, can be stored : {nums[idx] > sec_large_ele and nums[idx] < max_ele}")

print(sec_large_ele)

# print(max_ele)

# print(max(nums))
# print(min(nums))
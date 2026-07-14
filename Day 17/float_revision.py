nums = [10, 20, 30, 40, 50]
# print(max(nums))
max_element = float('-inf') # float

max_element = float('inf')
print(max_element)
nums = [-100000000000000000] #-100

n = len(nums)

for idx in range(n):
    if nums[idx] > max_element : 
        max_element = nums[idx]

print(max_element)

# CPP, Java
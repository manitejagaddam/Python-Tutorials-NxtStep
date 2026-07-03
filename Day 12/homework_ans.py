'''

find the maximum element in the list and the minimum element in the list

nums = [1, 5, 2, 6, 3, 7, 4, 90, 190, 11, 12, 14, 159, -1, -124, -178]
n = len(nums)
max_ele = 
min_ele = 

# Logic Part



print(f"Maximum element = {max_ele}") # 190
print(f"Minimum element = {min_ele}") #-178

'''



# nums = [1, 5, 2, 6, 3, 7, 4, 90, 190, 11, 12, 14, 159, -1, -124, -178]
# n = len(nums)
# max_ele = 
# min_ele = 

# # Logic Part



# print(f"Maximum element = {max_ele}") # 190
# print(f"Minimum element = {min_ele}") #-178




# Mukesh Code
nums = [1, 5, 2, 6, 3, 7, 4, 90, 190, 11, 12, 14, 159]
n = len(nums)

max_ele = float('-inf')
min_ele = float('inf')


for idx in range(n):
    if nums[idx] > max_ele:
        max_ele = nums[idx]
        
    if nums[idx] < min_ele:
        min_ele = nums[idx]


print(f"Maximum element = {max_ele}") # 190
print(f"Minimum element = {min_ele}") #-178
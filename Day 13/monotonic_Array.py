'''
Monotonic: -> Increasing Order 
    1 2 3 4 5 6 7 8
    10 12 14 16 17 20
    230 240 256 280 490 567 689
    
    
Non Monotonic -> Need Not to be an Increasing order
    1 3 2 5 4 7 6 9 8
    13 12 15 16 17 18 19
    123 134 156 15 167 189 190

'''



def isMonotonic(nums):
    # Code Block
    # 123, 134, 156, 15, 167, 189, 190
    #      idx
    n = len(nums)
    
    for idx in range(1, n, 1):
        if nums[idx] < nums[idx - 1] :
            return False
    
    # retrun true or flase
    return True



nums1 = [123, 134, 156, 15, 167, 189, 190]

nums2 = [1, 3, 5, 7, 9, 11, 13]

print(isMonotonic(nums1))  # False
print(isMonotonic(nums2))  # True
print(isMonotonic([230, 240, 256, 280, 490, 567, 689]))

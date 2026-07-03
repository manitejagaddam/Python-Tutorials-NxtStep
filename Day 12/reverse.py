num = [10, 20, 30, 40, 50, 60, 70, 80]
# [80, 70, 60, 50, 40, 30, 20, 10]


# def swap(a, b):
    # temp = a
    # a = b
    # b = temp

n = len(num)
idx1 = 0
idx2 = n - 1

while idx1 < idx2:
    # swap(num[idx1], num[idx2])
    # temp = num[idx1]
    # num[idx1] = num[idx2]
    # num[idx2] = temp
    
    num[idx1], num[idx2] = num[idx2], num[idx1]
    
    idx1 = idx1 + 1
    idx2 = idx2 - 1
print(num)
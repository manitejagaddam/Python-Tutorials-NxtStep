# arr = [12, 10, 5, 6, 52, 36]
# k = 2 

# 12 10
# 5 6 52 36
# 5 6 52 36 12 10

# Mukesh Code
# nums=[12,10,5,6,52,36]
# k = 4

# num1=nums[k:]
# print(num1)

# # .extend()

# num1.append(12)
# num1.append(10)

# print(num1)

nums=[12,10,5,6,52,36]
k = 4
# num2 = [12, 10, 5, 6]
num2 = nums[:k]

num1=nums[k:]
# print(num1)

num1.extend(num2)
print(num1)



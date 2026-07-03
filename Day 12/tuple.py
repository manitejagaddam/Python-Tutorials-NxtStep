# tuple -> constant list


'''

list -> []
set -> {}
tuple -> ()

'''


nums = (10, 20, 30, 40, 50)

lis = list(nums)

lis.append(60)
print(lis)

nums = tuple(lis)

print(nums)
# nums = [10, 20, 30, 40, 50]

# target = int(input("Enter your number to search : "))

# Nivedith Code
nums=[10, 20, 30, 40, 50, 60, 70]


target = int(input("Enter your number to search in the list : "))


print(type(target))
print(type(nums))
n = len(nums)

number_exits = 0

for idx in range(0, n, 1):
    
    if target==nums[idx]:
        number_exits = 1

if(number_exits == 1) :
    print("Number exits")
else : 
    print("Number dosen't exits")
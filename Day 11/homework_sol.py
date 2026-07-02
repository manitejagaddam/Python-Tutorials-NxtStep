'''
1. nums = [10, 20, 30, 40, 50, 60, 70]

Functions -> 
    1. Addition of all numbers in the list
    2. Multiplication of all numbers in the list
    3. Sqare of all numbers in the list
    4. power of all numbers in the list
    5. Even or Odd printing of all the numbers in the list
    
    1. addition(nums): -> integer
    2. multiplication(nums) -> integer
    3. Sqare of all number sqare(nums) -> print all sqares (no return)
    4. power of all number power(nums, 4) -> print all powers (no return)
    5. even_odd(nums) -> print even or odd (no return)

'''

def addition(nums):
    sum_val = 0
    n = len(nums)
    for idx in range(n):
        sum_val = sum_val + nums[idx]
        
    return sum_val

def multiplication(nums):
    multi_value = 1
    n=len(nums)
    for idx in range(n):
        multi_value = multi_value * nums[idx]
    return multi_value

def sqares_of_numbers(nums):
    n = len(nums)
    for idx in range(n):
        print(nums[idx] ** 2, end = " ")
    print()

def power_of_numbers(nums, power):
    n=len(nums)
    for idx in range(n):
        print(nums[idx] ** power, end = " ")
    print()

def even_or_odd(nums):
    n=len(nums)
    for idx in range(n):
        if (nums[idx] % 2 == 0):
            print("even number", end = " ")
        else:
            print("Odd number", end =  " ")
    print()

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



print(addition(nums)) # 55
print(multiplication(nums)) #
sqares_of_numbers(nums) # 1 4 9 16 25 36 49 64 81 100
power_of_numbers(nums, 3) # 1 8 27 64 81 125 216 ......
even_or_odd(nums) # odd even odd even odd even odd even odd even




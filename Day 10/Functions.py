'''

Functions ->    1. A program
                2. A celebration
                
    A set of program (or) code which can be reusable


'''

'''

nums = [10, 20, 30, 41, 51, 61, 70, 80, 91]

output -> 
        10 is an even number
        20 is an even number
        30 is an even number
        41 is an odd number
        51 is an odd number
        61 is an odd number
        70 is an even number
        80 is an even number
        91 is an odd number

'''


# Mukesh Code
# nums=[10,20,30,41,51,61,70,80,91]

# n=len(nums)

# for idx in range(n):
#     if (nums[idx] % 2 == 0):
#         print(f"{nums[idx]} -IT IS AN EVEN NUMBER")

#     else:
#         print(f"{nums[idx]} - IT IS AN ODD NUMBER")


# # Nivedith Code
# nums = [10 ,20, 30, 41, 51, 61, 70, 80, 91]

# n=len(nums)
# for idx in range (n):
#     if  nums[idx]%2==0 :
#         print(f"{nums[idx]} is an even number ;")

#     if nums[idx]%2!=0:
#         print(f"{nums[idx]} is an odd number ;")



# Sai Varun Code
# nums=[10, 20,30,41,51,61,70,80,91]

# n=len(nums) 

# for idx in range (n) :
#     if (nums[idx] %2  ==0) :
#         print(f"{nums[idx]} -IT IS AN EVEN NUMBER ") 
#     elif (nums[idx] %2 != 0) :
#         print(f" {nums[idx]} -IT IS AN ODD NUMBER")



def isEvenNumber(num):
    if num % 2 == 0:
        return True
    else :
        return False


def isPrime(num):
    factor_val = 2  # 1 and itself

    for idx in range(2, num, 1):
        if (num % idx == 0):
            factor_val = factor_val + 1
    
    
    if (factor_val == 2):
        return True
    elif (factor_val > 2):
        return False









nums=[10, 20,30,41,51,61,70,80,91]

n = len(nums)

for idx in range(n):
    if (isPrime(nums[idx])) :
        print(f"{nums[idx]} is a Prime Number")
    else :
        print(f"{nums[idx]} is not a Prime Number")
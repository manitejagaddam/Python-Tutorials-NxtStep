# Loops - For Loops and Range Function

# Why loops? Instead of repeating code many times, use loops

# Manual increment (repetitive):
# num = num + 1
# num = num + 1
# num = num + 1
# ... (repeat 20 times)

# Better approach - using loops:
# loop 20 times:
#     num = num + 1


# -------- RANGE FUNCTION --------
# range(start_index = 0, end_index, step_count = 1)

# Examples:
# for idx in range(10, 20, 2):
#     num = num + 1

# for variable_name in range(20):  # 0 to 19
#     num = num + 1


# -------- FOR LOOP EXAMPLES --------

# Example 1: Print numbers from 0 to 9 incrementing
# num = 1
# for variable_name in range(0, 10):
#     print(num)
#     num = num + 1


# Example 2: Print numbers from 100 to 149
# num = 100
# for idx in range(100, 150):
#     print(num)
#     num = num + 1


# -------- HOMEWORK CHALLENGES --------
'''
1. Print even numbers till 100
   0 2 4 6 8 10 12 14 16 18 ......... 100

2. Print odd numbers till user input
   100 -> 1 3 5 7 9 11 ......... 99
   1000 -> 1 3 5 7 9 11 ..............999
'''

# Solution Example: Print numbers with step
# for num in range(0, 101, 2):  # even numbers
#     print(num)

# for num in range(1, 100, 2):  # odd numbers
#     print(num)

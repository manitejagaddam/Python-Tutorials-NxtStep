# Sum of all the numbers till the user input value


'''

1. take the user input value
2. calculate the sum of n numbers till the user input

eg : 
    n = 3
    1 + 2 + 3 => 6  
    
    n = 10 
    1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 => 55

'''


num = int(input("Enter your Last Number : "))

sum_val = 0

for idx in range(1, num + 1, 1):
    # print("Idx value :  " + str(idx) + "  Sum Value : " + str(sum_val))
    sum_val = sum_val + idx


print(sum_val)

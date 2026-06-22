# Multiplication of all the numbers


'''

1. take the user input
2. print the multiplication of all the numbers till the input

eg: 
    1. 3
        1 * 2 * 3 => 6
    
    2. 5
        1 * 2 * 3 * 4 * 5 => 120

'''



# Num=int(input ("enter your last num : ")) 

# Multiple_val = 1

# for idx in range (1, Num + 1, 1) :
#     Multiple_val=Multiple_val*idx

# print(Multiple_val)




num = int(input("Enter your Last Number : "))

sum_val = 1

for idx in range(1, num + 1, 1):
    # print("Idx value :  " + str(idx) + "  Sum Value : " + str(sum_val))
    sum_val = sum_val * idx


print(sum_val)

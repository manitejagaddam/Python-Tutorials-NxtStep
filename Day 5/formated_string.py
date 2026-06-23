num = int(input("Enter any number : "))

'''

    5 x 1 = 5
    5 x 2 = 10
    5 x 3 = 15 ..........

'''


# input() -> string 
# int(input()) -> integer

# num = 10 -> integer
# str(num) -> string


'''

    " 5    x   1     =        5 " 
     num  str idx   str    num * idx
     
     variable + string + variable + string + varaible
     num      +   x    +    idx    +  =    +    num *  idx
'''


# 10 + 20 => 30 int + int = int

# first_name + last_name => string ==> string + string = string


# integer + string => 


for idx in range(1, 11, 1):
    # print(str(num) + " X " + str(idx) + " = " + str(num * idx))
    print(f"{num} X {idx} = {num * idx}")
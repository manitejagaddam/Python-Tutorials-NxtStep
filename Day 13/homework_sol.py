# Mukesh Code
# num=123456789

# #lst=[int(list) for list in str(num)]
# lst=list(str(num))
# print(lst)

# # Reverse of list
# n=len(lst)
# idx1=0
# idx2=n-1
# while  idx1<idx2:
#     lst[idx1],lst[idx2]=lst[idx2],lst[idx1]
    
#     idx1=idx1+1
#     idx2=idx2-1
    
# num = ''.join(lst)
# print(num)


'''
num -> break into digits and store in the list

[9, 8, 7, 6, 5, 4, 3, 2, 1]

combine the above digits in the list to a number.
'''

num = 123456789
lst = []
while num != 0:
    digit = num % 10
    # print(digit)
    lst.append(digit)
    num = num // 10
    
print(*lst)


num1 = 0

for digit in lst:
    num1 = num1 * 10
    # print(f"Mulplication -> {num1}")
    num1 = num1 + digit
    # print(f"Number -> {num1}")

print(num1)
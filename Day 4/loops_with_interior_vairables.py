# num = 0

# for variable_name in range(0 => variable_name = 0, 100, 1 => variable_name = variable_name + 1):
# for variable_name in range(0 => variable_name = 0, 100, 2 => variable_name = variable_name + 2):
# for variable_name in range(0, 100, 2):
#     # print(num)
#     # num = num + 2
#     print(variable_name)


''' 
1 to user input numbers print without using num variable

100
 1 2 3 4 5 6 7 8 9 10 ............. 100
 
1000 
 1 2 3 4 5 6 7 8 9 10 .............................. 1000

2
 1 2
'''



idx = int(input("Enter your idx number: "))

for i in range(0, idx, 1):
    print(i)

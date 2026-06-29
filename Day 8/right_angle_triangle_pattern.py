'''

n = 5

*
* *
* * *
* * * *
* * * * * 


'''



# # Meghana Code
# for i in range(1, 6):
#     print("* " * i)


# Nivedith Code
# n=int(input())

# for idx1 in range(0,n,1):
#     for idx2 in range(0,idx1 + 1,1):
#         print("*" , end=" ")
#     print()


# Meghana Code
# for i in range(1, 6):      
#     for j in range(i):      
#         print("*", end="")
#     print()





'''

1
1 2 
1 2 3 
1 2 3 4
1 2 3 4 5

'''



# Meghana Code
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=" ")
#     print()

# Nivedith Code
n=int(input())

for i in range(0,n+1,1):
    for j in range (1,i):
        print(j , end = " ")
    print()
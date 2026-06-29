


'''

n = 5 
***** -> A
***** -> A
***** -> A
***** -> A
***** -> A


'''

n = int(input())


# ***** -> A

for idx1 in range(0, n, 1):
    for idx2 in range(0, n, 1):
        print("*", end = ' ')
    print()




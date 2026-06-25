print("Enter your Range: ")
num=int(input())


# 5 * 2 = 10
# 5 -> number
# 2 -> index
# 10 -> ans

# 1 -> 10

# for number in range(1, num):
#     # Table Code
#     for index in range(1, 11): 
#         print(f"{number} x {index} = {number * index}")
#     print()

for idx1 in range(1, num + 1, 1):
    for idx2 in range(1, num + 1, 1):
        print("*", end = " ")
    print()


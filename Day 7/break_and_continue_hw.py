'''

print all the numbers from 1 to user input number 
1. if the number is a multiple of 5 print-> multiple of 5
2. if the number is a multiple of 7 print -> multiple of 7
3. if the number is multiple of both 5 and 7 -> dont print that number

'''

# # Nivedith Code
# for idx in range(1, 101, 1):
#     if idx %7==0 and idx %5==0:
#         continue
#     # print("The number which is not divisible by 7 or 5 is: ", idx)
#     elif idx %7==0 :
#         print("Divisible by 7" )
#         continue
#     elif idx %5==0:
#         print("Divisible by 5")
#         continue
#     print(idx)



# # Mukesh Code
# for idx in range (1,100,1):
#     if( idx % 5  == 0 and idx % 7 == 0):
#         continue
#     elif(idx % 5 == 0):
#         print("Divisible by 5")
#         continue
#     elif (idx % 7 == 0):
#         print("Divisible by 7")
#         continue
        
#     print(idx)



# # Meghana Code
# num = int(input("Enter a number: "))

# for i in range(1, num + 1):
#     if i % 5 == 0 and i % 7 == 0:
#         continue
#     elif i % 5 == 0:
#         print(f"{i} - Multiple of 5")
#     elif i % 7 == 0:
#         print(f"{i} - Multiple of 7")
#     else:
#         print(i)
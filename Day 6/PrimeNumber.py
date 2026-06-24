# Prime Number


# Mukesh Code
num=int(input("ENTER YOUR NUM"))

factor_val = 2  # 1 and itself

for idx in range(2, num, 1):
    if (num % idx == 0):
        factor_val = factor_val + 1


if (factor_val == 2):
    print( f"{num} IS A PRIME NUMBER ")
elif (factor_val > 2):
    print(f"{num} IS NOT A  PRIME NUMBER")
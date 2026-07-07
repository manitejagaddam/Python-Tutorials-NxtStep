num = 12345678
print(num)

while num != 0:
    digit = num % 10
    print(digit)
    num = num // 10


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 123456789

num1 = 0

for digit in digits:
    num1 = num1 * 10
    print(f"Mulplication -> {num1}")
    num1 = num1 + digit
    print(f"Number -> {num1}")

print(num1)

# Count how many elements are even/odd in an array.

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


even_count = 0
odd_count = 0

# Logic Part
n=len(nums)

for idx in range (n):
    if (nums[idx] % 2 == 0):
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

print(f"Even Count -> {even_count}")
print(f"Odd Count -> {odd_count}")

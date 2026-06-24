# elif - Else If Statements

'''
Control flow structure:
    if (condition):
        # code block
    
    elif (condition):
        # code block

    else:
        # code block
'''

# Homework Problem: Grade System with elif
'''
Grade Classification:
    91 - 100 -> A+
    81 - 90  -> A
    71 - 80  -> B+
    61 - 70  -> B
    51 - 60  -> C
    below 50 -> Just pass
'''

import time


# Correct implementation using elif:
marks = int(input("Enter your Marks : "))

start_time = time.time()
if (marks >= 91 and marks <= 100) :
    print("A+ Grade")
elif (marks >= 81 and marks <= 90):
    print("A  Grade")
elif (marks >= 71 and marks <= 80):
    print("B+  Grade")
elif (marks >= 61 and marks <= 70):
    print("B  Grade")
elif (marks >= 51 and marks <= 60):
    print("C  Grade")
else :
    print("Just Pass")

end_time = time.time()

print(f"Difference in time : {end_time - start_time}")
# Key difference: elif stops checking after first match, unlike multiple if statements

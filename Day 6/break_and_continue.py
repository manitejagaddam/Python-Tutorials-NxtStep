'''
keywords learned till now:
    1.  print()
    2.  input()
    3.  if
    4.  else
    5.  and
    6.  or
    7.  elif
    8.  f (formate)
    9.  for 
    10. in
    11. range()
    12. type()
    13. len()
    14. int()
    15. str()
    
    16. break
    17. continue



Opeators Learned till Now:
    1. +
    2. -
    3. *
    4. /
    5. % (Modulus Operator -> used to give remainder as output)
    6. ==
    7. != 
    8. <=
    9. >=
    10. <
    11. >
    12. ** (power operator)
    
'''



'''
Break -> spliting one part into two parts
                (or)
      -> giving gap
      -> stops anything
      -> stops a program


[1 2 3 4 5 6 7 8 9 10 | ............... 100]
for idx in range(1, 100, 1):
    if(idx == 10):
        break



continue -> 
    1. starting a broken program
    2. not stoping
    
    
    skips the present index
    
    
    1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 .......... 100
    
    
'''


# for idx in range(1, 100, 1):
#     print(idx)
#     break



# for idx in range(1, 10, 1):
#     if(idx == 5):
#         continue
#     print(idx)


# print every number till 100 except multiples of 3

# 1 2 (3) 4 5 (6) 7 8 (9) 10 11 (12) 13 14 (15) ..... (99) 100

# for idx in range(1, 100, 1):
#     if (idx % 3 == 0):
#         continue
#     print(idx)
    
    
# for idx in range(1,100,1):
#     if idx % 7 == 0:
#         continue
#     print(idx)


'''

1. take start index as 0 and end index as 10000 
2. take user input as last number 
3. print numbers from 0 to last number


 for idx in range(0, 10000, 1):
 
 input = 10 
 output = 1 2 3 4 5 6 7 8 9 10

'''
# Nivedith Code
# print("Enter your Number: ")
# num=int(input())
# for idx in range(0, 100000, 1):
#     if(idx == num + 1):
#         break
#     print(idx)


# # Meghana Code
# last_num = int(input("Enter the last number: "))

# for i in range(0,1000,1):
#     if i > last_num:
#         break
#     print(i)


# HOME WORK PROBLEM
'''

print all the numbers form 1 to user input number 
1. if the number is a multiple of 5 print-> multiple of 5
2. if the number is a multiple of 7 print -> multiple of 7
3. if the number is multiple of both 5 and 7 -> dont print that number

1
2
3
4
multiple of 5
6
multiple of 7
8
9
multiple of 5
11
12
13
multiple of 7
multiple of 5
16
17
18
19
20
multiple of 7
22
23
24
25
26
27
multiple of 7
29
30
31
32
33
34

36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69

71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99


'''

# for idx in range(1, 100):
#     print(idx)

# for idx in range(1, 100, 1):
#     if idx %7==0 and idx %5==0:
#         continue
#     print(idx)
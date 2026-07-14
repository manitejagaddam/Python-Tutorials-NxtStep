'''

List -> [10, 20, 30, 40, 50, 60]
        [0 , 1 , 2 , 3 , 4 , 5 ]

    nums[0] -> 10
    nums[3] -> 40
    
    {012 : 10
    123 : 20
    234 : 30
    345 : 40 
    456 : 50
    567 : 60}
'''

# {key, value}
dictionary = {12 : 10,
    123 : 20,
    234 : 30,
    "python" : "coding lang",
    456 : 50,
    567 : 60}

print(dictionary["python"])

dictionary[12345] = 89

print(dictionary)
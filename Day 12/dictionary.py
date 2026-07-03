'''
    key value -> pair
    
    hello -> greeting 
    python -> a programing language or snake

    dic =  {"python" : "snake", 
            "hello" : "greeting"}

list -> []
tuple -> ()
set ->  {}
dictionary -> {:}


'''






dic =  {"hyderabad" : 36,
        "warangal" : 32,
        "karminagar" : 34,
        "bhupalpally" : 30}

lis = [36,32,34,30,31]

dic['khammam'] = 31

print(dic['warangal'])
print(dic.get("khammam"))



lis = []
tup = ()
st = set()
dic = {}

print(type(lis))
print(type(tup))
print(type(st))
print(type(dic))
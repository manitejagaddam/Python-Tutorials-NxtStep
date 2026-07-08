'''
    OOPS Concept -> Object Oriented Programming System

    1. Class
    2. Object
    3. 4 Pillars

'''


# def list_reverse():
#     nums = [1, 2, 3, 4, 5, 6]

#     rev_nums = nums[::-1]

#     print(rev_nums)



# def main():
#     list_reverse()

# if __name__ == "__main__":
#     main()



# class Calculator:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
        


#     def addition(self):
#         return self.a + self.b
    
#     def subtraction(self):
#         return self.a - self.b
    
#     def multiplication(self):
#         return self.a * self.b
    
#     def division(self):
#         return self.a / self.b
    
#     def modulo(self):
#         return self.a % self.b
    
#     def power(self,power_val):
#         #print a to the power of power_val
#         #print b to the power of power_val
#         return self.a**power_val,self.b**power_val
    
#     def sqare(self):
#         return self.a**2,self.b**2
    
#     def cube(self):
#         return self.a**3,self.b**3
    
#     def less_than_or_equalls(self):
#         return self.b <= self.a
    
#     def greater_than_or_equalls(self):
#         return self.a >= self.b 
    
#     def sqare_root(self):
#         return self.a**0.5 , self.b**0.5


# py = Calculator(20,10)



# print(py.addition())
# print(py.subtraction())
# print(py.multiplication())
# print(py.division())
# print(py.modulo())
# print(py.power(4))
# print(py.sqare())
# print(py.cube())
# print(py.less_than_or_equalls())
# print(py.greater_than_or_equalls())
# print(py.sqare_root())





'''

4 Pillars
    1. Abstraction
    2. Encapsulation
    3. Inherritance
    4. Polymorphism   - Runtime , compile 

'''


# class A:
#     def __init__(self):
#         print("Class A")
        
#     def printA(self):
#         print("Class A")

# class B (A):
#     def __init__(self):
#         print("Class B")


# obj = B()
# obj.printA()





print(max(10, 20))
print(max([10, 20, 30, 40, 50, 60]))
print(max((10, 20, 30, 40, 50, 60)))


# def maxi(a, b):
#     return max(a, b)

def maxi(a, b, c = 10, d= 23):
    return max([a, b, c, d])


print(maxi(10, 20))
print(maxi(10, 20, 30))
print(maxi(10, 20, 30, 40))
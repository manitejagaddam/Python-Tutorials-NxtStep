a = 10
b = "name"

# list, tuple, set, dictionary







class Claculator:
    def print_hello(self):
        print(self)
        print("Hello Guys!")
        
    def __init__(self, num1, num2):
        print("Constructor Called")
        self.a = num1
        self.b = num2

    def addition(self):
        return self.a + self.b

    def subtraction(self):
        return self.a - self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


# print(Claculator().addition())
# print(Claculator().print_hello())

python_cal = Claculator(10, 20)
print(python_cal.addition())
print(python_cal.subtraction())
print(python_cal.multiplication())
print(python_cal.division())

# nums = []

# nums.



'''

a = 10
b = 20

addition()
subtraction()
multiplication()
division()

'''

class Number:
    def sum(self):
        return self.a + self.b

num = Number( )
num.a = 12
num.b = 34
s = num.sum( )
print(s)


# Object --->

#Class Railway form:
    

# class Attributes --->

class Employee:
    company = "Google"

salary = 100

harry = Employee( )
rajni = Employee( )
harry.salary = 45
rajni.salary = 400
print(harry.salary)
#print(rajni.salary)
#Employee.company = "Youtube"
#print(harry.company)
#print(rajni.company)


# Self Parameter -- >

class Employee:
    company = "Google"
    def getsalary(self):
        print(f"salary is {self.salary}")

harry = Employee( )
harry.salary = 100000
harry.getsalary( )



# Static Method ------- >

class Employee:
    company = "Google"

    def getsalary(self):
        print(f"salary for this employee working in {self.company} is {self.salary}")

    @staticmethod
    def greet( ):
        print("Good Morning,Sir")

harry = Employee( )
harry.salary = 100000
harry.greet( )



# _ _ init _ _( ) Constructor --- >



   
# Problem 01-->
class programmer:
    company = "Microsoft"
    def __init__(self,name,product):
        self.name = name
        self.product = product

    def getInfo(self):
         print(f"The name of the programmer is {self.name} and the product is {self.product}")

harry = programmer("Harry" , "Skype")
Alka = programmer("Alka" , "Github")

harry.getInfo( )
Alka.getInfo( )


# Problem 02 -->

class calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print("The value of {self.number} square is {self.number**2}")

    def squareRoot(self):
        print("The value of {self.number} squareRoot is {self.number**0.5}")

    def cube(self):
        print("The value of {self.number} cube is {self.number**3}")

a = calculator(3)
a.square( )
a.squareRoot( )
a.cube( )


# Problem 03 --->

class sample:
    a = "Harry" # class Attribute
obj = sample( ) # obeject/ Instace Attribute
obj.a = "Vikky"
print(sample.a)
print(obj.a)


# Problem -- >

class calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"The value of {self.number} square is {self.number**2}")

    def squareRoot(self):
        print(f"The value of {self.number} squareRoot is {self.number**0.5}")

    def cube(self):
        print(f"The value of {self.number} cube is {self.number**3}")

    @staticmethod
    def greet( ):
        print("Hello there welcome to the best calculator of the world")

a = calculator(9)
a.square( )
a.squareRoot( )
a.cube( )


# Problem -->

class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getstatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats available in the train are {self.seats}")

    def fareInfo(self):
        print(f"The price of the ticket is:Rs {self.fare}")

    def bookticket(self):
        if (self.seats > 0):
            print("Your ticket has been booked! Your seat number is {self.seat}")
        else:
            print("Sorry this is full! Kindly try in tatkal")

intercity = Train("Intercity Express: 14015", 90, 300)
intercity.bookticket( )
intercity.getstatus( )
intercity.fareInfo( )











    






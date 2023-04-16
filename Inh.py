class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "Python"
    company = "Youtube"
    def getLanguage(self):
        print(f"The language is {self.language}")

e = Employee( )
e.showDetails( )

def showDetails(self):
    print("This is an programmer")

p = Programmer( )
p.showDetails( )
print(p.company)


# Types Of Inheritence -->

# 01) Single Inheritance

# 02) Multiple Inheritance 
class Employee:
    company = "Visa"
    ecode = 120
class Frelancer:
    company = "Fiverr"
    level = 0
class Programmer(Employee,Frelancer):
    name = "Rohit"

def upgradeLevel(self):
    self.level = self.level+1
    p.upgradelevel( )

p = Programmer( )
print(p.level)
print(p.company)


# 03) Multilevel Inheritance 
class Person:
    Country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("I am an Employee so I am breathing++")

class Programmer(Employee):
    company = "Fiverr"

    def getsalary(self):
        print(f"No salary to programmer")

p = Person( )
e = Employee( )
pr = Programmer( )
p.takeBreath( )
e.takeBreath( )
pr.takeBreath( )


# Super Method -- >

class Person:
    country = "India"
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        super( ).takeBreath( )
        print("I am a Programmer so I am breathing++")
        print("I am an Employee so I am breathing++")

class Programmer(Employee):
    company = "Fiverr"

    def getsalary(self):
        print(f"No salary to programmer")

p = Person( )
e = Employee( )
pr = Programmer( )
p.takeBreath( )
e.takeBreath( )
pr.takeBreath( )



class Person:
    country = "India"

    def __init__(self):
        print("Intializing Person...\n")
    def takeBreath(self):
        print("I am breathing...")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super( ).__init__( )
        print("Intializing Employee...\n")

    def getsalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        super( ).takeBreath( )
        print("I am an Employee so I am breathing++")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super( ).__init__( )
        print("Intializing Programmer...\n")

    def getsalary(self):
        print(f"No salary to programmer")

    def takebreath(self):
        super( ).takeBreath( )
        print("I am an Programmer so I am breathing++")
p = Person( )
e = Employee( )
pr = Programmer( )
p.takeBreath( )
e.takeBreath( )
pr.takeBreath( )

# Class Method -->

class Employee:
    company = "Camel"
    salary = 100
    location = "Delhi"

# Method that change the salary 

def changesalary(self,sal):  # add Instance salary
    #self.__class__.salary = sal
    self.salary = sal        # for add new salary and not to change the salary

@classmethod
def chnagesalary(cls,sal):
    cls.salary = sal
e = Employee( )
print(e.salary)

e.changesalary(455)
print(e.salary)

print(Employee.salary)


#Q1

# class Shape:
#     def area(self):
#         print("")
# class Rectangle(Shape):
#     def area(self,l,b):
#         return l*b

# class Circle(Shape):
#     def area(self,r):
#         return r*3.14*r
# d=Circle()
# print(d.area(3))

# c=Rectangle()

# print(c.area(5,3))

#Q2

# class Speak:
#     def speak(self):
#         print("Animal speaking")
# class Dog(Speak):
#     def bark(self):
#         print("Dog baarking")

# class Cat(Dog):
#     def meow(slf):
#         print("CaT MEOWWWWWW")
# class Cow(Cat):
#     def boow(slf):
#         print("Cow booow")
# d=Dog()
# d.bark()
# d=Cat()
# d.meow()
# d=Cow()
# d.boow()

#Q3

# class Car:
#     def start_engine(self):
#         print("Engine_started")
# class ElectricCar(Car):
#     def start_engine(self):
#         super().start_engine()

# class GasolineCar(ElectricCar):
#     def start_engine(slf):
#         super().start_engine()

# d=ElectricCar()
# d.start_engine()
# d=GasolineCar()
# d.start_engine()

#Q4

# class Employee:
#     def __init__(self,salary):
#         self.s=salary
#     def calculate_salary(self):
#         days=int(input("Enter number of days you worked""/n"))
#         ta=300*days
#         da=400*days
#         bonus=200*days
#         self.s=ta+da+bonus
# class Manager(Employee):
#     def salary(self):
#         basic_salary=100000
#         super().calculate_salary()
#         self.s=self.s+basic_salary
#         print("total salary: ",self.s)
# class Developer(Employee):
#     def sal(self):
#         basic_salary=50000
#         super().calculate_salary()
#         self.s=self.s+basic_salary
#         print("total salary: ",self.s)
# while True:
#     ch=int(input("1.Manager/n 2.Developer/n 3.Exit"))
#     if ch==1:
#         obj1=Manager(0)
#         obj1.salary()
#     elif ch==2:
#         obj2=Developer(0)
#         obj2.sal()
#     elif ch==3:
#         break

#Q5

# class BankAccount:
#     def __init__(self,deposit,withdraw):
#         self.s=deposit
#         self.s=withdraw
#     def deposit(self):




class BankAccount:
    def __init__(self,name,num,bal):
        self.name=name
        self.num=num
        self.bal=bal
    def deposit(self):
        amt=int(input("enter amount to deposit:"))
        self.bal+=amt
    def withdraw(self):
        amt=int(input("enter amt to deposit:"))
        self.bal-=amt
    def show_bal(self):
        print("Name",self.name,'\n',"accountNo:",self.num,'\n',"balance:",self.bal)
l=[]
def create():
    name=input("enter name:")
    accno=int(input("enter account no:"))
    bal=int(input("set balance:"))
    x=BankAccount(name,accno,bal)
    l.append(x)
while True:
    print('1.Create Account\n 2.Deposit\n 3.withdraw\n 4.exit')
    ch=int(input('enter the choice:'))
    if ch==1:
         create()
    elif ch==2:
        ac=int(input('Enter accno:'))
        for i in l:
            if ac ==i.num:
                i.deposit()
                i.show_bal()
    elif ch==3:
         ac=int(input('Enter accno:'))
         for i in l:
            if ac ==i.num:
                i.withdraw()
                i.show_bal()
    elif ch==4:
        print('invalid')
        break
        


       

        
   








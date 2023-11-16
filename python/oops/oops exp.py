#Q1

# class Circle:
#     def radius(self,radius):
#           r=radius
#     def area(self,r):
#          area=3.142*r*r
#          print("the area of the circle is:",area)

#     def fer(self,r):
#          fer=2*3.14*r
#          print("the circumference of the circle is:",fer)

# C=Circle()
# radius=int(input("enter the radius of circle:"))
# C.area(radius)
# C.fer(radius)

#Q2

# while True:
#     choice=int(input("1.c to f calculator""\n""2.f to c calculator""\n""3.exit""\n""enter your choice""\n"))
#     if choice ==1:
#         class Temp:
#             def __init__(self,c):
#                 self.celc=c
#             def conf(self):
#                 a=((self.celc)*(9/5))+32
#                 print("f:",a)

#         cel=int(input("enter the c you want to convert"")\n"))
#         temp1=Temp(cel)
#         temp1.conf()
#     elif choice ==2:
#         class Temp:
#             def __init__(self,f):
#                 self.far=f
#             def conc(self):
#                 c=((self.far)-32)*(5/9)
#                 print("c:",c)

#         faren=int(input("enter the f you want to convert""\n"))
#         temp1=Temp(faren)
#         temp1.conc()
#     elif choice==3:
#         break
#     else:
#         print("wrong choice")

#Q3

# class Student:
#     def __init__(self,name,roll_no,):
#         self.name=name
#         self.roll_no=roll_no
#         self.age=None
#         self.mark=None

#     def Display(self):
#         print("Name:",self.name)
#         print("roll number:",self.roll_no)
#         print("age:",self.name)
#         print("marks:",self.mark)

#     def set_age(self,age):
#         self.age=age

#     def set_mark(self,mark):
#         self.mark=mark


# student1=Student("Arjun",1)

# student1.set_age(15)
# student1.set_mark(90)
# student1.Display()


# student2=Student("arun",2)

# student2.set_age(15)
# student2.set_mark(91)
# student2.Display()

# student3=Student("Aju",3)

# student3.set_age(15)
# student3.set_mark(93)
# student3.Display()


#Q4

# class Time:
#     def __init__(self,hour,minutes):
#         self.hour=hour
#         self.minutes=minutes

#     def add_time(self,other):
#         self.minutes +=other.minutes
#         if self.minutes>=60:
#             self.hour +=1
#             self.minutes -=60

#         self.hour +=other.hour

#     def display_time(self):
#         print(f"{self.hour}):{self.minutes}")

#     def display_minutes(self):
#         print(self.hour*60+self.minutes)

# t1=Time(2,50)
# t2=Time(1,20)

# t1.add_time(t2)
# t1.display_time()
# t1.display_minutes()




        

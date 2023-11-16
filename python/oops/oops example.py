# class calc:
#     def __init__(self,a,b):
#         self.n=a
#         self.m=b
#     def add(self):
#         self.sum=self.n+self.m
#         print(self.sum)
#     def sub(self):
#         self.sub=self.n-self.m
#         print(self.sub)
# k=int(input("enter no:"))
# p=int(input("enter no:"))
# ob=calc(k,p)
# ob.add()
# ob.sub() 

# Q1

# class Bank:
#     def __init__(self,name,accno,balance):
#         self.name=name
#         self.m=accno
#         self.balance=balance
#     def deposit(self):
#         amt=int(input("enter amount:"))
#         self.balance+=amt
#         print(self.balance,"is balance")
#     def withdrawal(self):
#         amt=int(input("enter amt to withdraw:"))
#         self.balance-=amt
#         print(self.balance,"is balance")
# name=input("enter name:")
# accno=int(input("enter accno:"))
# balance=int(input("set balance:"))
# B1=Bank(name,accno,balance)
# B1.deposit()
# B1.withdrawal()


# Q2

# class Bank:
#     def __init__(self,name,num,bal):
#         self.name=name
#         self.num=num
#         self.bal=bal
#     def deposit(self):
#         amt=int(input("enter amount to deposit:"))
#         self.bal+=amt
#     def withdraw(self):
#         amt=int(input("enter amt to deposit:"))
#         self.bal-=amt
#     def show_bal(self):
#         print("Name",self.name,'\n',"accountNo:",self.num,'\n',"balance:",self.bal)
# l=[]
# def create():
#     name=input("enter name:")
#     accno=int(input("enter account no:"))
#     bal=int(input("set balance:"))
#     x=Bank(name,accno,bal)
#     l.append(x)
# while True:
#     print('1.Create Account\n 2.Deposit\n 3.withdraw\n 4.exit')
#     ch=int(input('enter the choice:'))
#     if ch==1:
#          create()
#     elif ch==2:
#         ac=int(input('Enter accno:'))
#         for i in l:
#             if ac ==i.num:
#                 i.deposit()
#                 i.show_bal()
#     elif ch==3:
#          ac=int(input('Enter accno:'))
#          for i in l:
#             if ac ==i.num:
#                 i.withdraw()
#                 i.show_bal()
#     elif ch==4:
#         print('invalid')
#         break
        




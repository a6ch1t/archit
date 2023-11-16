# example:

#function program


#function declaration
# def pattern1():


#function definition
#     k=1
#     for i in range(6):
#         for j in range(1,k+1):
#             print("*",end=" ")
#         k=k+2
#         print()


# def pattern2():
#     for i in range(10):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print()

#function call
# pattern1()
    

# Q1

# def capitailed():
    
#     l2=[]
#     i=0
#     m=str(input("enter the string:\n"))
#     n=m.split()
#     while i<len(n):
#         b=n[i]
#         l2.append(b[0].upper()+b[1:])
#         i+=1
#     sr=" ".join(l2)
#     print(sr)

# capitailed()

# Q2

# def nnn():
#     m=str(input("enter the string:\n"))
#     b=""
#     i=0
#     while i<len(m):
#         if m[i].isalpha():
#             b=b+m[i]
#         i=i+1
#     print(b)
# nnn()

# Q3

# nums=[2,5,8,9]
# for i in nums:
#     print(i)
# square=[]
# for i in nums:
#     square.append(i*i)
# print("The square of","is",square)

# Q4

# def sum():
#     a=int(input("enter the string:"))
#     b=a%10
#     c=a//10
#     d=c%10
#     e=c//10
#     sum=(b**2)+(d**2)+(e**2)
#     print(sum)
# sum()

# Q5

# a=[1,2,3,4]
# b=[2,2,5,6,4]
# c=[]
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print(c)

# *********************************************

# Q1

# def fib(n):
#     a,b=0,1
#     while a<=n:
#         print(a,end=" ")
#         a,b=b,a+b
# num=int(input("enter the number"))
# if num<=0:
#     print("enter positive integer")
# else:
#     print("fib num less than or equal to",num,"are:")
#     fib(num)

# Q2

# num=[3,8,12,7,6,10,21,15]
# tarsum=18
# pairs=[]
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if num[i]+num[j]==tarsum:
#             pairs.append((num[i],num[j]))

# for pair in pairs:
#     print(pair)

# Q3

# def pair():
    
#     l=['apple','banana','cherry','date']
#     l2=[]
#     for i in range(len(l)):
#         a=l[i]
#         for j in range(len(l)):
#             b=l[j]
#             if a[i] in b[j]:
#                 l2.append((a,b))
#     print(l2)
# pair()
            
# Q4

# n=[2,3,4,5,6]

# for i in range(len(n)):
#     for j in range(i+1,len(n)):
#         p=n[i]*n[j]
#         s=n[i]+n[j]
#         if p%2==0 and s%2!=0:
#             print(f"pair:({n[i]},{n[j]})")
 

#*************************************************

#Q1

# s=input("enter a sentence ")
# w=s.split()
# word_count=len(w)
# print(f"number of words in the sentence:{word_count}")



    
    
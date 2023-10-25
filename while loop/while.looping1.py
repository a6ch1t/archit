

# exp
# i=2
# n=int(input("enter number"))
# while i<n:
#     print("Hello")
#     i=i+1


# Q.01
# d={}
# n=input("enter the word:")
# i=0
# while i<len(n):
#     if n[i] in d:
#         d[n[i]]+=1
#     else:
#         d[n[i]]=1
#     i=i+1
# print(d)




   # Q.02 
# l3=[]
# i=0
# l1=("11","22","3")
# l2=("3","2","11")
# while i<len(l1):
#     if l1[i] in l2:
#         l3.append(l1[i])
#         i=i+1
#         print(l3)



# Q.03
# r=""
# n=input("enter word:")
# i=len(n)-1
# while i>=0:
#     r+=n[i]
#     i=i-1
# print(r)    


# Q.04
# l=['dogg','cat','cow']
# i=0 
# while i<len(l):
#     m=len(l[i])
#     print(l[i],m)
#     i=i+1


# Q.05
# s=0
# l1=[]
# n=int(input("enter no. of elements:"))
# i=1
# while i<=n:
#     p=int(input("enter the no:"))
#     l1.append(p)
#     print(l1)
#     s+=p
#     i=i+1
# print(l1,s)


# Q.06
# i=0
# n=4
# l1=[]
# while i<=n:
#     p=int(input("enter the no:"))
#     l1.append(p)
#     i=i+1
# l1.sort()
# print("largest elements is:", l1[-1])


# Q.07

# n=str(input("enter the words:"))
# i=0
# b=1
# while i<len(n):
#    if n[i].isalpha():
#       pass
#    else:
#       b=b+1
#    i=i+1
# print(b)

# Q.08

# i=0
# l2=[]
# l1=["apple","cat","orange","mango","dog"]
# while i<len(l1):
#     if len(l1[i])>=5:
#         l2.append(l1[i])
#     i=i+1
# print(l2)
    
# Q.09
# l1=[10,2,4,5,6,9]
# l2=[]

# i=0

# while i<len(l1):
#     if l1[i]%2==0:
#         l2.append(l1[i])
        
#     i=i+1

# print(l2)
      
    # Q.10   
     
# l1=["apple","orange","grape","mango"]
# l2=[]
# i=0
# while i<len(l1):
#     l2.append(l1[i].capitalize())
#     i=i+1
# print(l2)    
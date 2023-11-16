#000000000000000000000000000000000000000000000000                           
#0###############################################
#0#*******************************************##0
#0#*******************************************##0
#0#**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**##0
#0#**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**##0
#0#**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!                                     !**##0
#0#**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**##0
#0#**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**##0
#0#**!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!**##0
#0#*******************************************##0
#0#*******************************************##0
#0###############################################
#000000000000000000000000000000000000000000000000

# Q1

# a=4
# i=0
# b="*"
# for i in range(a):
#     print(b)
#     b=b+"*"
#     i=i+1

# or
# for i in range(1,5):
#     for j in range(i):
#         print("*",end="")
#     print()


# Q2

# for i in range(4,0,-1):
#     for j in range(i):
#         print("*",end="")
#     print()

# Q3

# n=4
# for i in range(5):
#     for k in range(0,n):
#         print(end=" ")
#     n-=1
#     for j in range(0,i+1):
#         print("*",end="")
#     print()

# Q4

# n=1
# for i in range(4,0,-1):
#     for k in range(0,n):
#         print(end="")
#     n+=1
#     for j in range(i):
#         print("*",end=" ")
#     print()

# *********************************
# Q1

# for i in range(1,4):
#     for j in range(1,i+1):
#         print(j,end=" ")
#         j=j+1
#     print()
    

# Q2

# h=1
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(h,end=" ")
#         h=h+1
#     print()

# Q3

# for i in range(1,4):
#     for j in range(1,i+1):
#         # if j%2==0:
#             print(j*2,end=" ")
            
#     print()

# Q4

# h=2
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(h,end=" ")
#         h=h+2
#     print()

# Q5

# for i in range(4):
#     k=1
#     for j in range(1,i+1):
#         print(k,end=" ")
#         k=k+2
#     print()


# Q6

# h=1
# for i in range(1,4):
#     for j in range(1,i+1):
#         print(h,end=" ")
#         h=h+2
#     print()


# Q7

# for i in range(4):
#     for j in range(i+1,0,-1):
#         print(j,end=" ")
        
#     print()

# Q8

# for i in range(1,5):
#     for j in range(1,i+1):
#         if j%2==0:
#             print('2',end=" ")
#         else:
#             print('1',end=" ")
#     print()



# # Q9

# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=" ")
#         j=j+1
#     print()

# for i in range(4):
#     for j in range(i+1,0,-1):
#         print(j,end=" ")
        
#     print()
# # ************************************

# -ASCII-

# Q1

# for i in range(1,4):
#     k=65
#     for j in range(1,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()

# Q2

# for i in range(65,68):
#     for j in range(65,i+1):
#         print(chr(i),end=" ")
      
#     print()


# Q3

# k=65
# for i in range(65,68):
    
#     for j in range(65,i+1):
#         print(chr(k),end=" ")
#         k=k+1
#     print()


# Q4

# for i in range(64,68):
#     for j in range(i+1,64,-1):
#         print(chr(j),end=" ")
        
#     print()

# Q5

# n=6
# for i in range(6):
#     for k in range(0,n):
#         print(end="  ")
#     n-=1
#     print("*",end=" ")
#     for j in range(1,i+1):
#         print(chr(65),end=" ")
#         print("*",end=" ")
        
#     print()

# Q6

# n=6
# for i in range(5):
#     for k in range(0,n):
#         print(end="  ")
#     n-=1
#     for j in range(1,i+1):
#         print(j,end=" ")
#     for m in range(i-1,0,-1):
#         print(m,end=" ")
#     print()

# Q7





# for i in range(1,7):
#     for j in range(1,i+1):
#         if i%2==0:
#           print("*",end=" ")
#         else:
#            print(j,end=" ")
#     print()


# Q8

# b=4
# a=(b*2)+1
# for i in range(a):
#     for k in range(0,1):
#         print("*",end=" ")
#     if i<b:
#         for j in range(1,i+1):
#             print(j,end=" ")
#         for m in range(i-1,0,-1):
#             print(m,end=" ")
#     if i>=b:
#         for n in range(1,b):
#             print(n,end=" ")
#         for o in range(b,0,-1):
#             print(o,end=" ")
#         b=b-1
#     if i>0 and i<a-1:
#         for l in range(0,1):
#             print("*",end=" ")
#     print()



    




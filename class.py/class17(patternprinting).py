#Pattern printing

#squares of stars
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

"""for i in range(5):
    for j in range(5):
        print("*" ,end =" ")
    print()"""


#Left triangle of stars

# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

"""for i in range(1,6):
    for j in range(1,i+1):
        print("*",end= " ")
    print()"""

#Inverted right triangle of stars

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

"""n = 5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*" , end = " ")
    print()"""

"""n = 5
for i in range(n,0,-1):
    for j in range(1,i):
        print("*" , end = " ")
    print()"""

#
    #  * * * * * 
    #  * * * * * 
    #  * * * * * 
    #  * * * * * 
    #  * * * * * 

"""n = 5
for i in range(1,n+1):
    for j in range(n):
        print("" , end=" ")
    for k in range(n):
        print("*" , end=" ")
    print()"""

# increasing number triangle

# 1
# 12
# 123
# 1234
# 12345

"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j ,end="")
    print()"""


# inverted number traingle
# 12345
# 1234
# 123
# 12
# 1

"""n = 5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j ,end="")
    print()"""


#Leftt-Aligned Triangle
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 

"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()"""

#
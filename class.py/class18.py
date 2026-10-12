#right parallelogram of stars

# *****
#   *****
#    *****
#     *****
#      *****

"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,n+1):
        print("*",end="")
    print() 
"""

#left parallelogram of stars

#      *****
#     *****
#    *****
#   *****
#  *****

"""n = 5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(" ",end="")
    for k in range(1,n+1):
        print("*",end="")
    print() """

#Question   

#  *****
#   *****
#    *****
#     *****
#      *****
#     *****
#    *****
#   *****
#  *****

"""n = 5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(" ",end="")
    for k in range(1,n+1):
        print("*",end="")
    print() 
for i in range(1,n):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(1,n+1):
        print("*",end="")
    print() """


# Right - Aligned triangle 

#     *
#    **
#   ***
#  ****
# *****

"""n= 5
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for k in range(i):
        print("*",end="")
    print()    """

# Inverted Rigjt - Aligned triangle
# *****
#  ****
#   ***
#    **
#     *

"""n= 5
for i in range(1,n+1):
    for j in range(1,i):
        print(" ",end="")
    for k in range(1,n-i+2):
        print("*",end="")
    print() """

# Full pyramid
#     *
#    ***
#   *****
#  *******
# *********
  
"""n = 5
for i in range(1,n+1):
    #for space
    for j in range(n-i):
        print(" ",end="")
    #for stars    
    for k in range(2 * i - 1):
        print("*",end="")
    print() """       


# Inverted full pyramid
# * * * * * * * * * 
#   * * * * * * * 
#     * * * * * 
#       * * * 
#         * 
  
"""n = 5
for i in range(n,0,-1):
    #for space
    for j in range(1,n-i+1):
        print(" ",end=" ")
    #for stars    
    for k in range(2 * i - 1):
        print("*",end=" ")
    print() """    


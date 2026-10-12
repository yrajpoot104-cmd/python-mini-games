#Functions

"""def hello():
    print("how are you")

for i in range(10):
    hello()"""

#Parameters and arguments
#whenever we want to accep a value in a function you have to use parameters

# def additional(a,b): # -> parameters
#     print(a+b)

#and whenever you want to provide values to those
#parameters you have to use arguments

# additional(12,12) #-> positional arguments
# additional(10,20)

#return
"""
def hello():
    return "hello yash"

a = hello()
print(a)"""

#Question

"""def strongnumber(n):
    sum = 0
    temp = n
    while n != 0:
        a = n%10
        fact = 1
        for i in range(1,a+1):
            fact = fact * i 
        sum = sum + fact
        n //= 10

    if sum == temp:
        print(temp)
for i in range(1,100000):
    print(strongnumber(i))"""
    
    
#types of parameters and arguments

# default parametres
# we have to provide a default value to our paramteres
# but it cannot be created before a normal parameters

"""def additional(a,b = 10, c = 30):
    print(a+b+c)

additional(10)
"""
#positional arguments

"""def xyz(a,b,c):
    print(a,b)

xyz(12,c=45,b=45)    """

#Q1. Add Two Numbers
# Create a function add() that takes two numbers
# as arguments and returns their sum.

"""def additional(a,b):
    print(a+b)

additional(10,20)"""

#Q2. Check Even or Odd
# Create a function check_even_odd() that takes 
# a number and returns whether it is Even or Odd.

"""def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("enter a number :")) 
result = check_even_odd(num)
print(result)   """

#Q3. Find Square
# Create a function square() that takes
# a number and returns its square.

"""def square(num):
    return num * num

num = int(input("enter a number :"))
result = square(num)
print(result)"""

#Q4. Find Maximum
# Create a function maximum() that takes two numbers
# and returns the greater number.
"""
def maximum(a,b):
    if a > b:
        return a
    else:
        return b

a = int(input("enter a first number :"))
b = int(input("enter a second number :"))

print("maximum number =",maximum(a,b))"""

#Q5. Check Number
# Create a function check_number() that takes a number
# and checks whether it is Positive, Negative, or Zero.

"""def check_number(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

# number = int(input("enter the number :"))
print(check_number(2))"""


#Q6. Calculate Simple Interest
# Create a function simple_interest() that takes
# P, R, and T and returns the Simple Interest.
"""
def simple_interest(p,r,t):
    return (p * r * t)/100

p = int(input("enter principal :"))
r = float(input("enter rate :"))
t = int(input("enter time :"))

print("simple interest =",simple_interest(p,r,t))"""

#Q7. Find Cube
# Create a function cube() that takes a number
# and returns its cube.

"""def cube(n):
    return n ** 3
num = int(input("enter number :"))
print(cube(num))"""

#Q8. Check Voting Eligibility
# Create a function eligible() that takes age as an argument.
# If age is 18 or above, return "Eligible",
# otherwise return "Not Eligible".

"""def eligible(n):
    if n >= 18:
        return "eligible"
    else:
        return "not eligigble"
    
n = int(input("enter the age :"))
print(eligible(n))"""

#Q9. Find Factorial
# Create a function factorial() that takes 
# a number and returns its factorial.

"""def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact*i
    return fact    

n = int(input("enter the number :"))
print(factorial(n))"""


#Q10. Count Digits
# Create a function count_digits() that takes
# a number and returns the total number of digits.

"""def count_digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count     

n = int(input("enter the number :"))
print(count_digit(n))   """

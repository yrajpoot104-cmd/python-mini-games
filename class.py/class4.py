#operators
#types of operators :-
#1)Arthimetic operators
#2)Logical operators
#3)Comparasion operators 
#4)Assignment operators
#5)Conditional operators

#Arthimetic operators
#(+,-,*,/,//,%,**,)

a = 30
b = 20
print(a + b) #ouput -> 50
print(a - b)  #ouput -> 10
print(a * b)  #ouput -> 600
print(a/b)  #ouput -> 1.5
print(20/5)  #ouput -> 4.0
print(int(20/5))  #ouput -> 4 not use this

print((20//5)) #output -> 4 # it will remove the values after decimal

print(5**2) #output -> 25 # this is for power operation
print(62//5) #output -> 12
print(12%5) #output -> 2 # it will find reminder -> 2

# take inputs of principal , rate and time  and find out 
# the simple interest (P*R*T/100)
# khud k try kiya hua(-_-)
# a = 5
# b = 10
# c = 15

# d = a*b*c
# e = (a*b*c/100)
# print(d)
# print(e)

# take inputs of principal , rate and time  and find out 
# the simple interest (P*R*T/100)

# P  = int(input("enter the principal amount:"))
# R = float(input("enter the rate:"))
# T = int(input("enter the Timme in years:"))

# si = (P*R*T)/100
# print(f"your simple intrest is {si}")

#compount operators

# P  = int(input("enter the principal amount:"))
# R = float(input("enter the rate:"))
# T = int(input("enter the Timme in years:"))

# ci = (P*(1+(R/100))**T) - P
# print(f"The c.i. {ci}")

#assignment operators 
 
a=12
a+=60
print(a)
b=10
b=b+10
print(b)

a=10
a+=20
a-=30
a+=10
a//=2
a*=2
print(a)
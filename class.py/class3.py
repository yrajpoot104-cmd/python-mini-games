#type conversion
# 1) int() , float() , str() , bool()

#when you want to convert from one data type two another 
#you have to use type conversion

#int float and string are basic but if we talk about bool 
#there are some falsy values - (0,0.0,"",False,[],(),{},None)

a = 10
a = str(a)
print(type(a))

a = 10.5
a = str(a)
print(type(a))

a = True
a = str(a)
print(type(a))

a = 13
a = float(a)
print(a)

a = 13.25
a = int(a)
print(a)

a = 10
b = 55.25
c = ""
d = 0
e = "25.3"
print(bool(a))
print(bool(b))
print(bool(c))
print(bool(d))
print(bool(e))

#inputs and outputs
#for providing the output you have only one thing ans that is 
#print()
#how you can use variables while printing 
# name = "yash"
# age = 20

# print("hello how are you")
# print(name)
# print("and your age is")
# print(age)

#print("hello how are you",name,"and your age is",age)

#2nd way is more simple
#print(f"hello how are you {name} and your age is {age}")

name = input("what is your name :")
age = int(input("what is your age :"))
temp = float(input("what is the temp :"))


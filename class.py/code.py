#Question 1

# age = int(input("enter the temperature :"))
# if temp > 30:
#     print("high temperature")
# else:
#     print("normal temperature")


#Question 2

# balance = int(input("enter the available balance :"))
# amount = int(input("enter the amount :"))
# if balance <= 2500:
#     print("transaction approved")
# else:
#     print("transaction rejected")



#Question 3

# age = int(input("enter the age :"))
# if age >= 18:
#     print("candidates is eligible")
# else:
#     print("candidates is not eligible")


#Question 4

# marks = int(input("enter the marks :"))
# if marks >= 50:
#     print("student will be pass")
# else:
#     print("student will be fail")


#Question 5

# password = int(input("enter the password :"))
# if password == 12345:
#     print("correct password")
# else:
#     print("incorrect password")


#Question 6 

# amount = int(input("enter the amount :"))
# if amount >= 2000:
#     print("receive discount")
# else:
#     print("no discount")


#Question 7

# nums = int(input("enter the number :"))
# if nums > 0:
#     print("number is positive")
# else:
#     print("number is non positive")


#Question 8

# attendance = int(input("enter the attendance :"))
# if attendance >= 75:
#     print("student are eligible")
# else:
#     print("student are not eligible")


#Question 9 

# pin = int(input("enter the pin :"))
# if pin == 9999:
#     print("access granted")
# else:
#     print("access denied")


#Question 10

# order = int(input("enter order value :"))
# if order >= 1000:
#     print("receive free delivery")
# else:
#     print("delivery charge applicable")


#Question 1
"""n=int(input("enter numbers :"))
count = 0
for i in range(n):
    if i%3 and i%5 ==0:
        count += 1
print(count)"""

#Question 2

"""n=int(input("enter number :"))
for i in range(2,n):
    if n%i==0:
        print("not a prime number")
        break 
    else:
        print("prime number")
        break"""

#Question 4
"""a = int(input("enter tha 1 number :"))
b = int(input("enter the 2 number :"))
if a>b:
    for i in range(b,0,-1):
        if a%i ==0 and b%i ==0:
            print(f"HCF is {i}")
            break
elif b>a:
    for i in range(a,0,-1):
        if b%i ==0 and a%i ==0:
            print(f"HCF is {i}")
else:
    print(f"HcF is {i}")"""

#Question 3

# a=int(input("enter the number :"))
# count = 0
# while(a>0):
#     a//=10
#     count+=1
# print(count)

#1)
#Variable
"""name = "Laptop"
price = 50000
quantity = 2

total = price * quantity
print(total)

#Lists

items = ["Apple","Bread","Milk"]
print(items)
print(items[0])

#Dictionary

item = {
    "name": "laptop",
    "price": 50000,
    "quantity": 2
}
print(items[name])
print(items[price])
print(items[quantity])"""

for i in range(5):
    for j in range(5):
        print("*" ,end =" ")
    print()

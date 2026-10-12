#sum of digits eg - 123 - 6

"""n = int(input("enter the number :"))
sum = 0
while n != 0:
    sum = sum + n%10
    n//=10

print(sum)"""

# #print the reverse of a number -eg - 123
"""
n = int(input("enter the number :"))
rev = 0
while n != 0:
    rev = rev * 10 + n % 10
    n //= 10

print(rev)"""


#palindrome number - 1221 - 1221
"""
n = int(input("enter a number :"))
rev = 0
temp = n
while n != 0:
    rev= rev*10+n%10
    n //= 10

print(rev)
if temp == rev:
    print("palindrome number")
else:
    print("not palindrome number")"""

#number guessing game (1-100)

"""import random
num = random.randint(1,100)
count = 0

while True:
    count += 1
    guess = int(input("guess your number between 1-100 "))
    if guess == num:
        print(f"congratulation you won in {count} times")
        break 

    elif guess > num:
        print("go a bit lower")

    else:
        print("go a bit higher")"""

#.....

#Question 
#check the perfact number

"""n=int(input("enter number :"))
sum = 0
for i in range(1,n):
    if n % i ==0:
        sum += i

if sum == n:
    print("perfact number")
else:
    print("not a perfact")"""

#print fibonacci series up to n terms 

"""n=int(input("enter the number :"))
a = 0
b = 1
for i in range(n):
    print(a,end=" ")
    c = a+b
    a = b
    b = c"""

#minimum currency notes breakdown
"""amount = int(input("enter the amount :"))
temp_amount=amount 
min_notes = 0
while amount > 0:
    if amount >= 500:
        count500 = amount // 500
        amount = amount % 500
        min_notes += count500
        print(f"500 notes -> {count500}")

    elif amount >= 200:
            count200=amount // 200
            amount = amount % 200
            min_notes += count200
            print(f"200 notes -> {count200}")

    elif amount >= 100:
            count100= amount // 100
            amount = amount % 100
            min_notes += count100
            print(f"100 notes-> {count100}")

    elif  amount >= 50:
            count50 = amount // 50
            amount = amount % 50
            min_notes += count50
            print(f"50 notes-> {count50}")  

    elif amount >= 20:
            count20 = amount // 20
            amount = amount % 20
            min_notes += count20
            print(f"20 notes -> {count20}")

    elif amount >= 10:
                count10= amount // 10
                amount = amount % 10
                min_notes += count10
                print(f"10 notes -> {count10}")

print("total minimum notes =",min_notes)"""


#Square
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 

"""for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print() """


#right triangle
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print() """


#inverted right triangle
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

"""n = 5
for i in range(1,n+1):
    for j in range(1,n-i+2):
        print("*",end=" ")
    print() """

#increasing number triangle
# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5 

"""for i in range(1,n+1):
    for j in range(1,i+1):
        print(j , end=" ")  
    print() """   

#inverted number triangle
# 1 2 3 4 5 
# 1 2 3 4 
# 1 2 3 
# 1 2 
# 1 

"""for i in range(1,n+1):
    for j in range(1,n-i+2):
        print(j , end=" ")
    print() """

#sum of digits eg - 123 - 6

"""n = int(input("emter the number :"))
sum = 0
while n != 0:
    sum = sum + n%10
    n //= 10
print(sum) """

#print the reverse of a number -eg - 123

"""n = int(input("enter the number :"))
rev = 0
while n != 0:
    rev = rev*10 + n%10
    n //= 10
print(rev) """   


#palindrome number - 1221 - 1221

"""n = int(input("enter number :"))
rev = 0
temp = n
while n != 0:
    rev = rev*10+n%10
    n //= 10
print(rev) 
if rev == temp:
    print("palindrome number")
else:
    print("not a palindrome number") """   




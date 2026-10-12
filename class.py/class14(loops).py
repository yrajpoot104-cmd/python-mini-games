#sum of digits eg - 123 - 6

"""n=int(input("enter the number :"))
sum = 0
while n != 0:
    sum = sum + n%10
    n = n//10

print(sum)"""

#print the reverse of a number -eg - 123

"""n=int(input("enter the number :"))
rev = 0
while n != 0:
    rev = rev*10+n%10
    n = n//10
print(rev)"""

#palindrome number - 1221 - 1221

"""n=int(input("enter the number :"))
temp = n
rev = 0
while n != 0:
    rev = rev*10+n%10
    n = n//10
print(rev)
if temp == rev:
    print("palindrome number")
else:
    print("not palindrome")"""

#Q1. Reverse a Number
# Take an integer N as input and print its reverse

"""n=int(input("enter number :"))
rev = 0
while n != 0:
    rev = rev*10+n%10
    n //= 10
print(rev)"""

#Q2. Check Palindrome Number
# Take an integer N as input and check whether the number remains the same
# when its digits are reversed

"""n=int(input("enter number :"))
temp = n
rev = 0
while n != 0:
    rev = rev*10+n%10
    n //= 10
print(rev)
if temp == rev:
    print("palindrome number ")
else:
    print("not palindrome")"""


#Q3. Count Digits Greater Than 5
# Take an integer N as input and count
# how many digits in the number are greater than 5

"""n=int(input("enter number :"))
count = 0
while n > 0:
    digit = n%10
    if digit > 5:
        count += 1
    n //= 10
print("digit gtreater than 5:",count)"""

#Q4. Product of Digits
# Take an integer N as input and
# calculate the product of all its digits

"""n=int(input("enter number :"))
product = 1
while n > 0:
    digit = n%10
    product = product * digit
    n //= 10
print("product of digits :",product)"""


#Q5. Check Whether a Number Contains Digit 7
# Take an integer N as input and check whether
# the digit 7 is present in the number

"""n=int(input("enter number :"))
found = False 
while n > 0:
    digit = n%10
    if digit == 7:
        found = True
        break
    n //= 10
if found:
    print("7 is present")
else:
    print("7 is not present")"""

#Q6. Count Digits Divisible by 3
# Take an integer N as input and count
# how many digits are divisible by 3, including 0

"""n = int(input("enter number :"))
count = 0
while n > 0:
    digit = n%10
    if digit % 3 == 0:
        count = count + 1
    n //= 10
print("count:",count)"""




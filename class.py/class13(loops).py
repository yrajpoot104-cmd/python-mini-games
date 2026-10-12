 #check  the number whether it is prime or not

"""n = int(input("enter numbers :"))
for i in range(2,n//2+1):
    if n%i == 0:
        print("composite number")
        break
else:
    print("prime number")"""


# n= int(input("enter your range :"))
# for j in range(2,n+1):
#     for i in range(2,j//2+1):
#         if j%i == 0:
#             break
#     else:
#         print(j)

#find the HCF of two numbers

# a = int(input("enter the smallest number :"))
# b = int(input("enter the greatest number :"))
# I= 0
# for i in range(1,a+1):
#     if a%i ==0:
#         if b%i ==0:
#             if i>I:
#                 I=i
# print(I)     

"""a=int(input("enter the 1 number :"))
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
    print(f"HCF is {a}")"""


# While loop

# a = 1
# while a > 0:
#     print(a)
#     a = a + 1 # output -> infinite


#separate the digit of 

# a = 5050440
# while a > 0:
#     print(a%10)
#     a = a//10

#Take an integer N as input and count
#  how many numbers from 1 to N are divisible by 3.

"""n = int(input("enter the number :"))
count = 0
for i in range(1,n+1):
    if i % 3 == 0:
        count += 1
print("count =",count)"""


#Take N numbers as input and determine the largest number among them.

"""a = int(input("enter how many numbers :"))
largest = 0
for i in range(a):
    num = int(input("enter number :"))
    if num > largest:
        largest = num
print("largest number =",largest)"""


#Take N numbers as input. Calculate their average.

"""n=int(input("enter how many numbers :"))
total = 0
for i in range(n):
    num = int(input("enter numbers :"))
    total += num

average = total / n
print("Average =",average)"""


#Take an integer N as input and check whether it is a perfect number.
#A perfect number is a number whose proper factors add up to the number itself.

"""N = int(input("enter a number :"))

sum = 0

for i in range(1, N):
    if N % i == 0:
        sum += i

if sum == N:
    print("Perfect number")
else:
    print("Not a perfect number")"""


#Take an integer N as input and print all the numbers
#  from 1 to N that are divisible by 10.

"""n = int(input("enter the numbers :"))
for i in range(1,n+1):
    if i % 10 == 0:
        print(i)"""
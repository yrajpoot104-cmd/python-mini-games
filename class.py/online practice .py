
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


# ATM system
"""
correct_pin = "1234"
attempts = 3

for i in range(attempts):

    pin = input("enter your PIN :")
    if pin == correct_pin:
        print("PIN verified successfully!")
        break
    else:
        print("incorrect PIN!")

else:
    print("card blocked please contact your bank")
    exit()

balance = 5000
while True:

    print("1.check balance")
    print("2.deposit cash")
    print("3.withdraw cash")
    print("4.exit")

    choice = input("enter your choice :")
    if choice=="1":
        print("current balance :",balance)

    elif choice =="2":
        amount = float(input("enter deposite amount :"))
        balance = balance + amount 
        print("updated balance :",balance)

    elif choice == "3":
        amount = int(input("enter withdrawal amount :"))

        if amount <= balance:
            balance = balance - amount 
            print("withdrawal successful")
        else:
            print("insufficient balance")
    elif choice == "4":
        print("thank you for using our ATM have a nice day !")
        break

    else:
        print("invalid choice! please choose 1-4")
"""

# Prime number from 1-n

"""for num in range(2,11):
    count = 0
    for i in range(1,num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        print(num)  """

# Check the number is Strong number 

"""n = int(input("enter a number :"))
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
    print("strong number")
else:
    print("not a strong number")"""            

# Armstrong number

"""n = int(input("enter a number :"))
temp = n
digits = len(str(n))
total = 0
while temp > 0:
    digit = temp % 10
    total = total + digit ** digits
    temp = temp // 10

if total == n:
    print("Armstong numbers")
else:
    print("not an Armstong number") """       

# check the palindrome number

"""n = int(input("enter the number :"))
temp = n
rev = 0
while n != 0:
    rev = rev*10+n%10
    n //= 10
print(rev)
if rev == temp:
    print("palindrome number")
else:
    print("not a plindrome number") """

           


































































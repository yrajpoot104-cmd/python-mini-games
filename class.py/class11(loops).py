#find the factors of n

"""n=int(input("enter numbers :"))
for i in range(1,n+1):
    if n%i==0:
        print(i)"""

#
# n = int(input("enter number :"))
# for i in range(1,n+1):
#     print(i)

#count the number of factorials of n

"""n=int(input("enter the number :"))
count = 0
for i in range(1,n+1):
    if n%i==0:
        count = count+1
print(count)"""

#check  the number whether it is prime or not

"""n=int(input("enter number :"))
count = 0
for i in range(2,n+1):
    if n%i==0:
        count = count + 1
if count ==2:
    print("prime number")
else:
    print("composite number")"""


# n = int(input("enter numbers :"))
# for i in range(1,n+1):
#     if n%i ==0:
#         print(i)


#Question

# n = int(input("enter numbers :"))
# count = 0
# for i in range(1,n+1):
#     if n%i ==0:
#         count = count + 1
# print(count)

#An institution records the attendance status of a student for **7 consecutive days**.
# The status is entered as P for Present and A for Absent.
#Write a program to determine the total number of days
#the student was present and absent.

"""present = 0
Absent = 0

for i in range(7):
    status = input("enter attendance (P/A): ")
    if status == "P":
        Present += 1
    elif status == "A":
        Absent += 1
print("total Present :",Present)
print("total Absent :",Absent)"""


#A factory inspects **10 products**.
#  For each product, enter 1 if it passes inspection and 0 if it fails.
# Determine the **number of products that passed and failed** the inspection.

"""passed = 1
failed = 0

for i in range(10):
    result = int(input("enter inspection result (1/0) :"))
    if result == 1:
        passed += 1
    elif result == 0:
        failed += 1
print("product passes :",passed)
print("product failed :",failed)"""


#Q3.motnhly savings analysis

# A person records the amount saved on **7 different days**.
# Write a program to calculate the **total savings** and
# determine how many days the savings were greater than ₹500.

"""total = 0
count = 0

for i in range(6):
    saving = int(input("enter saving :"))
    total = total + saving
    if saving > 500:
        count = count + 1
print("total savings :",total)
print("days savings were greater than 500:",count)"""


#Q4.Electricity Consumption

# A household records its electricity consumption for 7 days
# Write a program to calculate the **total units consumed** and
# count how many days the consumption was **more than 10 units**.

"""total = 0
count = 0

for i in range(7):
    units = int(input("enter electricity units :"))
    total = total + units
    if units > 10:
        count = count + 1
print("total units consumed :",total)
print("days with more than 10 units :",count)"""
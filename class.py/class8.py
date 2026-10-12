#Question 1

"""num = int(input("enter a num :"))
if num>0 and num>10:
    print("positive and greater that 10")
elif num>0 and num<10:
    print("positive and less than 10") 
else:
    print("non positive")"""      

"""num = int(input("enter a num :"))
if num>0:
    print("positive")
    if num > 10:
        print("and greater than 10")
    else:
        print("and less than 10")
else:
    print("non posotive")"""

#Question 2

"""num = int(input("enter a num :"))
if num%2 ==0 and num%4 == 0:
    print("even and div by 4")
elif num%2 == 0 and num%4 != 0:
    print("even and not div by 4")
else:
    print("odd number") """       


"""if num %2 == 0:
    if num%4 == 0:
        print("even and div by 4")
    else:
        print("event and not div by 4")
else:
    print("odd number") """

#Question 3

"""pin = int(input("enter the pin :"))
if pin == 1234:
    amount = int(input("enter the amount  "))
    if amount <= 5000:
        print("withdraw success")
    else:
        print("insufficient balance")
else:
    print("incorrect pin") """


#Question 4

"""num1 = int(input("enter the first number :"))
num2 = int(input("enter the second number :"))

if num1>=num2:
    if num1%2 == 0:
        print(f" {num1} is greater than {num2} and even ")
    else:
        print(f" {num1} is greater than {num2} and odd ")
else:
    if num2%2 == 0:
        print(f"{num2} is greater than {num1} and even ")
    else:
        print(f"{num2} is greater than {num1} and odd ")"""


#Question 5

"""num = int(input("enter the number :"))

if num == 0:
    print("number is zero")
elif num>0:
    if num%2 == 0:
        print("even and positive")
    else:
        print("odd and positive")
else:
    if num%2 == 0:
        print("even and neg")
    else:
        print("odd an neg") """


#Question 6
#check scholarship eligibility

"""percentage = float(input("enter the percentage :"))
income = int(input("enter your family income :"))
sports = input("sports achievement (yes/no): ")

if percentage >= 80:
    if income <= 300000:
        print("Full scholarship")
    else:
        if sports == "yes":
            print("partial scholarship")
        else:
            print("no scholarship")
elif percentage >= 60:
    if sports == "yes":
        print("sports scholarship") 
    else:
        print("not eligible")
else:
    print("not eligible")"""                               


#Question 7
#driving license eligibility

"""age = int(input("enter your age :"))
learner = input("learner license (yes/no):")
test = input("driving test passed (yes/no):")

if age < 18:
    print("not eligible") 
elif learner == "no":
    print("get learner license first") 
elif learner == "yes":
    if test == "yes":
        print("license approved")
    else:
        print("retake driving test")"""

#Question 8
# restaurant table booking

geust = int(input("number of geust : "))
table = input("table type (normal/private): ")   
occasion = input("special occasion (yes/no): ")

if table == "normal":
    if geust <= 6:
        print("booking available")
    else:
        print("choose private table") 
elif table == "private":
    if geust <= 10:
        if occasion == "yes":
            print("private table decoration")
        else:
            print("private table booked")
    else:
        print("maximum 10 geust") 
else:
    print("invalid table type")                              


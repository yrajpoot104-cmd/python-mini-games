# Lists methods

#append

# l = [10,20,30]
# l.append(40)
# print(l)

# print(dir(list))





# Questions
# reverse the list without using the methods of lists.
"""
a = [10,20,30,40,50]
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)    """


"""a = [10,20,30,40,50]
temp = len(a)-1
for i in range(0,(len(a)-1)//2):
    a[i],a[temp] = a[temp],a[i]
    temp = temp -1

print(a)    """


#Q1. Find the Smallest Element
# Create a list of numbers and find the smallest element
# without using the min() function.
"""
numbers = [12, 5, 23, 8, 17]
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
print(smallest) """


#Q2. Count Positive and Negative Numbers
# Create a list and count the number of positive
# and negative elements. Ignore zeros.

"""numbers =  [10, -5, 20, -8, 0, 7]
positive = 0
negative = 0

for num in numbers:
    if num > 0:
        positive = positive + 1
    elif num < 0:
        negative = negative + 1

print("positive numbers :",positive)
print("negative numbers :",negative)"""


#Q3. Calculate the Average
# Create a list of numbers and calculate the average of all its elements.

"""numbers = [10,20,30,40,]
total = 0

for num in numbers:
    total = total + num

average = total / len(numbers)
print(average)    
"""

#Q4. Count Occurrences of an Element
# Create a list and count how many times a given number appears in it.

"""numbers = [2,4,2,6,2,8]
count = 0
target = 2

for num in numbers:
    if num == target:
        count += 1

print(count)"""


#Q5. Print Elements at Even Indices
# Create a list and print the elements present at even indices (0, 2, 4, …).

"""numbers = [10,20,30,40,50,60]
for i in range(len(numbers)):
    if i % 2 == 0:
        print(numbers[i])"""


#Q6. Find the Second Largest Element
# Create a list and find the second largest distinct 
# element without using sort() or max().

"""numbers = [10,25,15,40,30]
largest = numbers[0]
second = None

for num in numbers:
    if num > largest:
        second = largest
        largest = num

    elif num < largest and (second is None or num > second):
        second = num

print("second largest :",second)  """


#Q7. Replace Negative Numbers with Zero
# Create a list and replace every negative element with 0.

"""numbers = [10,-5,20,-8,7]

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print(numbers)"""


#Q8. Find the Sum of List Elements
# Create a list of numbers and calculate the sum of all its elements.

"""numbers = [ 10,20,30,40]
total = 0

for num in numbers:
    total = total + num
print(total)    
"""

#Q9. Find the Largest Element
# Create a list of numbers and find the largest
# element without using the max() function.
"""
numbers = [12,45,23,67,34]
largest = numbers[3]
for num in numbers:
    if num > largest:
        largest = num
print(largest)"""


#Q10. Reverse a List
# Create a list and reverse its elements without 
# using the reverse() method.

"""a = [10,20,30,40,50]
b = []
for i in range(len(a)-1,-1,-1):
    b.append(a[i])
print(b)"""
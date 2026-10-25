# reverse the list without using the methods of lists.
#input = [10,20,30,40,50]
#output = [50,40,30,20,10]
"""arr = [10,20,30,40,50]
n = len(arr)
for i in range(0,n//2):
    arr[i],arr[n-i-1] = arr[n-i-1],arr[i]

print(arr)"""

# print positive and negative elements of a list


"""list = [10,-5,20,-3,0,8]
print("positive :")
for element in list:
    if element > 0:
        print(f"{element}")
print("negative :")        
for element in list:
    if element < 0:
        print(f"{element}")"""

# calculate the average of all elements in a list
#input = [10,20,30,40]
#output = 25.0

"""list = [10,20,30,40]
sum = 0
for i in list:
    sum += i

print(f"mean -> {sum/len(list)}")"""    

# find the greatest element and print its index.
#input = [2,96,69,77,145,20]
#output = max element = 145 found at 4 index
"""
list = [2,96,69,77,145,20]
max = list[0]
index = 0
for i in range(len(list)):
    if max < list[i]:
        max = list[i]
        index = i

print(f"{max} found at {index} index") """

#Q1. Separate Even and Odd Numbers**

#Create a list of integers and separate the even and odd numbers into two different lists.
# **Example:**
# - Input: [1, 2, 3, 4, 5, 6]
# - Output:
#     - Even: [2, 4, 6]
#     - Odd: [1, 3, 5]

"""list = [1,2,3,4,5,6]

print("even number")
for element in list:
    if element%2 == 0:
        print(f"{element}")
print("odd number")
for element in list:
    if element%2 != 0:
        print(f"{element}")"""


#Q2. Remove Duplicates**

# Create a list and remove duplicate elements without using set().
# **Example:**
# - Input: [1, 2, 3, 2, 4, 1, 5]
# - Output: [1, 2, 3, 4, 5]

"""list = [1, 2, 3, 2, 4, 1, 5]
empity_list = []
for num in list:
    if num not in empity_list:
        empity_list.append(num)

print(empity_list) """       


#**Q3. Find the Index of an Element**

# Create a list and find the index of a given element
# without using the index() method.
# **Example:**
# - Input: [10, 20, 30, 40, 50]
# - Element: 30
# - Output: 2
"""
list = [10,20,30,40,50]
target = 30
for i in range(len(list)):
    if list[i] == target:
        print(i)"""


#**Q4. Swap First and Last Elements**

# Create a list and swap its first and last elements.
# **Example:**
# - Input: [10, 20, 30, 40, 50]
# - Output: [50, 20, 30, 40, 10]

"""numbers =  [10, 20, 30, 40, 50]
numbers[0],numbers[-1]= numbers[-1],numbers[0]
print(numbers)"""


#Q5. Find the Second Smallest Element**

# Find the second smallest distinct element without using sort() or min().
# **Example:**
# - Input: [15, 5, 20, 8, 12]
# - Output: 8

"""numbers = [15, 5, 20, 8, 12]
smallest = float("inf")
second_smallest = float("inf")

for num in numbers:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num > smallest and num < second_smallest:
        second_smallest = num

if second_smallest == float("inf"):
    print("second smallest distinct element does not exist")
else:
    print(second_smallest) """               


#Q6. Multiply All Elements**

# Create a list and calculate the product of all its elements.
# **Example:**
# - Input: [2, 3, 4, 5]
# - Output: 120

"""numbers = [2,3,4,5,6]
product = 1
for num in numbers:
    product = product * num
print(product)"""    

#**Q7. Count Numbers Greater Than a Given Value**

# Create a list and count how many elements are greater than a given number.
# **Example:**
# - Input: [10, 25, 15, 40, 30]
# - Number: 20
# - Output: 3

"""numbers = [10,25,15,40,30]
target = 20
count = 0
for num in numbers:
    if num > target:
        count += 1
print(count) """       


#**Q8. Count Numbers Smaller Than a Given Value**

# Create a list and count how many elements are smaller than a given number.
# **Example:**
# - Input: [10, 25, 15, 40, 30]
# - Number: 20
# - Output: 2
"""
numbers =  [10, 25, 15, 40, 30]
count = 0
target = 20

for num in numbers:
    if num < target:
        count += 1
print(count) """


#**Q9. Merge Two Lists**

# Merge two lists into a single list without using the + operator.
# **Example:**
# - Input: [1, 2, 3] and [4, 5, 6]
# - Output: [1, 2, 3, 4, 5, 6]

"""list1 = [1,2,3]
list2 = [4,5,6]
merged = []

for num in list1:
    merged.append(num)

for num in list2:
    merged.append(num)

print(merged) """   


#**Q10. Print Elements at Odd Indices**

# Print all elements present at odd indices (1, 3, 5, …) of a list.
# **Example:**
# - Input: [10, 20, 30, 40, 50, 60]
# - Output: [20, 40, 60]

numbers = [10,20,30,40,50,60]
l=[]
for i in range(len(numbers)):
    if i % 2 != 0:
        l.append(numbers[i])
    
print(l)
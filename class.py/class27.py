#Q1. print each key
'''d = {"ravi":30, "Rohan":33, "chirag":22, "Devraj":100}

# method 1
print(d.keys())

# method 2
for i in d:
    print(i)

# method 3
for key, value in d.items():
    print(key)'''

#Q2. print sum of all the marks
'''d = {"ravi":30, "Rohan":33, "chirag":22, "Devraj":100}
total = 0
for i in d.values():
    total += i
print(total)'''    

#Q3. print student who scored more than 80
'''d = {"ravi":30, "Rohan":33, "chirag":22, "Devraj":100}
for name, marks in d.items():
    if marks >= 80:
        print(name)'''

#Q4. find and print the student with the highest marks using FOR LOOP ONLY
'''d = {"ravi":30, "Rohan":33, "chirag":22, "Devraj":100}
top = ""
highest = 0
for name,  marks in d.items():
    if marks > highest:
        highest = name
        top = name
print(top)
print(highest) '''     # doubt

#Q5. create a dictionary of numbers and their squares(1 to 5)
'''square = {}
for i in range(1,6):
    square[i] = i * i
print(square)'''    

#Q6. add 5 bonus mark to every student
'''d = {"ravi":30, "Rohan":33, "chirag":22, "Devraj":100}
for i in d:
    d[i] = d[i] + 5
print(d)  '''  

# practice sheet Questions
#Q1.Find the Largest Value
# Given a dictionary containing numbers, find the largest value without using max().
# Example:
# Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# Output: 40
'''d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
largest = 10
for value in d.values():
    if value > largest:
        largest = value
print("largest value:",largest)'''   

#Q2. Find the Smallest Value
# Given a dictionary containing numbers, find the smallest value without using min().
# Example:
# Input: {'a': 10, 'b': 25, 'c': 5, 'd': 40}
# Output: 5
'''d = {'a': 10, 'b': 25, 'c': 5, 'd': 40}
smallest = 10
for value in d.values():
    if value < smallest:
        smallest = value
print("smallest value:",smallest)'''  

#Q3. Count Even and Odd Values
# Count how many values in a dictionary are even and how many are odd.
# Example:
# Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# Output:
# Even: 2
# Odd: 2
'''d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
even_count = 0
odd_count = 0
for value in d.values():
    if value % 2 == 0:
        even_count += 1    
    else:
        odd_count += 1
print("even count:",even_count)
print("odd_count:",odd_count)'''             

#Q4. Sum of Even Values
# Find the sum of all even values present in a dictionary.
# Example:
# Input: {'a': 10, 'b': 15, 'c': 20, 'd': 7}
# Output: 30
'''d = {'a': 10, 'b': 15, 'c': 20, 'd': 7}
even_sum = 0
for value in d.values():
    if value % 2 == 0:
        even_sum += value        
print("even sum:",even_sum)'''  

#Q5. Find a Key with a Given Value
# Given a dictionary and a value, find the key associated with that value.
# Example:
# Input: {'a': 10, 'b': 20, 'c': 30}
# Value: 20
# Output: b
'''data = {'a': 10, 'b': 20, 'c': 30}
target = 20
for key, value in data.items():
    if value == target:
        print(key)'''


#Q6. Update All Values
# Increase every value in a dictionary by 5.
# Example:
# Input: {'a': 10, 'b': 20, 'c': 30}
# Output: {'a': 15, 'b': 25, 'c': 35}
'''d = {'a': 10, 'b': 20, 'c': 30}
for key in d:
    d[key] = d[key] + 5
print(d)'''    


#Q7. Count Values Greater Than a Number
# Count how many dictionary values are greater than a given number.
# Example:
# Input: {'a': 10, 'b': 25, 'c': 15, 'd': 40}
# Number: 20
# Output: 2
'''d = {'a': 10, 'b': 25, 'c': 15, 'd': 40}
count = 0
num = 20
for key in d:
    if d[key] > num:
        count += 1
print(count)'''


#Q8. Create a Dictionary from Two Lists
# Given two lists, create a dictionary where the first list contains keys
# and the second list contains values.
# Example:
# Keys: ['a', 'b', 'c']
# Values: [10, 20, 30]
# Output:
# {'a': 10, 'b': 20, 'c': 30}
Keys = ['a', 'b', 'c']
Values = [10, 20, 30]
d = {}
for i in range(len(Keys)):
    d[Keys[i]] = Values[i]
print(d)    
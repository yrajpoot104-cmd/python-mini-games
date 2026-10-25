# Tuple...
# A tuple is an orderd, immutable collection.
# Once you creste it, you can't change, add or remove itmes

#1. Annoted by (paranthesis)
#2. Orered -> their are indexex
#3. hetrogenous -> Mixed types values are allowed
#4. Duplicate Elements are allowed
#5. Immutable 
#6. 
'''t = () #Empty Tuple
print(type(t))
'''
'''t = (1,2,3,4)
print(t)'''

'''t = (1,2,3,4, "hello", 32.4,True)
print(t)'''

'''t = (1,2,3,4,4,5,5)
print(t)'''

'''t = (1,2,3,4)
t[3] = 100
print(t)'''

'''t = (1,2,3,4,5,6,7)
print(t)
print(t[1:5])
print(t[::-1])'''

# Methods
#1. count() -> count the occurence of any value 
#2. Index() -> Show the index location of the first occurence element
'''t = (1,2,1,2,1)
print(t.count(1))
print(t.index(2))'''

'''
OPERATIONS
+ -> two tuple can concatenate
* -> Repetition
'''
t1 = (1,2)
t2 = (3,4)
print(t1 + t2)
print("Hi" * 5)
print(t1 * 5)

t = (1,2, [1,2,3,4])
t[2].append(100)
print(t)


# SETS
"""
SETS
1. Sets are collection of Unique items.
2. Sets are annoted by {} or set()
Empty {} -> dict but {1,2,3,4} -> set.
3. Sets are Hetrogenous.
4. Sets are Unordered.
5. As Sets don't have indexing we cannot replace anyvalue
6. No Duplicates allowed.
"""

"""
s1 = {1,2,3,4,5,False, 80.2, "Sample"}
# s2 = set() Empty Set
print(s1)
"""


"""
l = [1,1,2,3,4,4,5]
print(set(l))
"""


#METHODS OF SET
#. .add() -> to add any element inside of set
s = {1,1,2,3}
s.add(4)

#. .remove() -> remove any element from set.
s.remove(3)
print(s)

#. .discard() -> if element is not present inside of set so it will not raise any error.
s.discard(6)
print(s)



"""
SET OPERATIONS...
1. UNION -> merge both the sets.
2. INTERSECTION -> Common elements
3. DIFFERENCE -> ese elements jo ek set but dusre mai nahi.
4. SYMMEETRIC DIFFERENCE -> Common elements remove krke deta hai.
"""
"""
print(f" UNION -> {s1.union(s2)}")
print(f" INTERSECTION -> {s1.intersection(s2)}")
print(f" DIFFERENCE -> {s1.difference(s2)}")




s1 = {1,2,3,4,5}
s2 = {4,5,6,7,8}
print(f"UNION -> {s1 | s2}")
print(f"INTERSECTION -> {s1 & s2}")#& AND
print(f"DIFFERENCE -> {s1 - s2}")
print(f"SYMMETRIC -> {s1 ^ s2}")
print(f" SYMMETRIC -> {s1.symmetric_difference(s2)}")
"""


s = frozenset([1,2,3,4,5])
s.add(6)
s.remove(1)
print(s)
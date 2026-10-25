# Dictionary
#1. Annoted by {curly brackets}
#2. Dictionary is combinations multiple keys:values
#3. Dictionary are Mutable
#4. Dictionary are Hetrogenous
#5. Dictionary are orderd
#6. In Dictionary keys will always be UNIQUE but values can be duplicate


"""d = {} # Empty dictionary
d = {1:10,2:20,3:30}
print(d[1])"""

"""d = {} # Empty dictionary
d = {1:10,2:20,3:30}
d[3] = 100
print(d)"""

"""d = {1:10,2:20,3:30,4:20} # 5:50
d[5] = 50 # Creating the new values and assiging values
print(d)"""

#agar hum direct loop run krte hai dictionary pe toh we will get keys
"""d = {1:10,2:20,3:30,4:20}
for i in d:
    print(i,d[i])"""


# Methods in Dictionary
# will give the values from the dictionary
#1.keys()
"""d = {"a":1.0, "b":2.0, "c":3.0, "d":10.89}
print(d.keys())"""

#2.values()
"""d = {"a":1.0, "b":2.0, "c":3.0, "d":10.89}
print(d.values())"""

#3.item()
#it will give both keys and values from the Dictionary
"""d = {"a":1.0, "b":2.0, "c":3.0, "d":10.89}
print(d.items())"""

#d.item() #it will give key and values
"""d = {"a":1.0, "b":2.0, "c":3.0, "d":10.89}
for key, value in d.items():
    print(key,value)"""

#d.pop() -> remove the key and value from the dictionary
d= {"a":1.0, "b":2.0, "c":3.0, "d":10.89}
d.pop("c")
print(d)
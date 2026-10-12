#comparision operators
#(==,>,<,>=,<=,!=)
# a = 10
# b = 20
# print(a == b) #left side and right side must be equal
# print(12.5 > 12) #it can compare between 2 datatypes
# print("A" == "A")
# print("ABC" < "ABD") #string compares on the basis of unicodes # output -> True 
# print("ABC" == "ABD") #output -> False

# print(13.8 > 78 ) #output = False
# print(bool("") == False ) # output = True
# print(12 > 12) #output = False
# print(12 >= 12) #output = true

# a = 10
# b = 20
# c = 30
# print(c>a,c>b) #output = True True

#when you want to get a single result out of multiple
#comparision you have to use logical operators
#(and , or, not)

#and logical operators says all the comparision must be 
#True
print(12 == 12 and 45 != 23 and 60 > 50 and 34 != 34) # output = False

#or logical operators says out of all the comparision 
#only one must be True
print(12 == 45 or 45 == 67 or 23 == 23) #output = true

# not logical operators convert True -> False and
# False -> True
print(15==15) #output = True
print(not 15 == 15) #output = False

print((12 == 45 or 23 ==45 or not 12 != 12) and (bool (34) and 34 ==34 ))

#strings
# name = "Harsh"
# print(ord("K"))
# print(ord("a"))
# print(ord("A"))
# print(ord("B"))
# every thing inside a string has a 
# unique code and to find that you have 
# to use ord()

#indexing
#every element inside your string 
#can be accessed using index
#there are two types of indexing 
#one is positive starting from 0
#and one is negative starting from -1
s = "ROBOT 922"
print(s[-5],s[4])# output - T T

#slicing
#whenever you want to extract a portion
#of your string you can use slicinig 
#there are 3 points in slicing [start,stop,step]
#and these 3 points take index values of
#your string
s = "ROBOT 922"
print(s[0:5:1]) #output -> ROBOT
print(s[6:9:1]) #output -> 922

#default values of slicing 
a = "ROBOT 922"
print(a[6::1])
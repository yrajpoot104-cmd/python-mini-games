#Question 
#the list in the Ascending order
#Bubble sort
#example:
#input = [64,34,25,12,22,11,9]
#output = [9, 11, 12, 22, 25, 34, 64]
"""list = [64,34,25,12,22,11,9]
n = len(list)
for j in range(n):
    for i in range(n-1-j):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]

print(list)"""                        

#list Questions
# Find the pair with the given sun
#Find all pairs of elements whose sum euqal a givem target
#Example:
#input = [2,4,3,5,7,8]
#target = 10
#output:
#(2,8)
#(3,7)
'''arr = [2,4,3,5,7,8]
target = 10
n = len(arr)
for i in range(n):
    for j in range(i+1,n):
        if(arr[i] + arr[j]) == target:
            print(arr[i],arr[j])'''

# write a python program to check whether all elements
#  of one list appear consecutively in another list
#Example:
#input: 
#arr= [10 20,30,40,50]
#sub = [20,30,40]
#ouput = sublist found
arr = [10,20,30,40,50]
n = len(arr)
sub = [20,30,40]
m = len(sub)
for i in range(0,n-m+1):
    if arr[i:i+m] == sub:
        print("sublist found")
        break
else:
    print("not sublist found")
# Find the missing number 
# A list contains numbers from 1 to n but one number
# is missing write a program to find the missing number
#example:
#input = [1,2,4,5]
#output = missing number = 3

arr = [1,2,4,5]
n = len(arr)
og_n = n +1
og_sum = ((og_n)*(og_n+1))//2

# we solve this by formula and by loop
# og_sum = 0
# for i in range(1,og_n+1):
#     og_sum += i

real_sum = 0
for elem in arr:
    real_sum += elem
missing = og_sum - real_sum
print(missing)

# check if the list elements are arranged in ascending order.
#example:
#input = [10,20,30,40,50]
#output = list is sorted

"""arr = [10,20,30,40,50]
n = len(arr)
is_sorted = True
for i in range(0,n-1):
    if arr[i] > arr[i+1]:
        is_sorted = False
        break
if is_sorted:
    print("list is sorted")
else:
    print("list is not sorted") """


# check whether the list read the same fro front and back
#example:
#input = [2,3,15,15,3,2]
#output = palindrome list

"""list =  [2,3,15,15,3,2]
palindrome = True
n = len(list)
for i in range(n-1//2):
    if list[i] != list[n-i-1]:
        palindrome = True
        break
if palindrome:
    print("list is palindrome")
else:
    print("not a palindrome")"""        



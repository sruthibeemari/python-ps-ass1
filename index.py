# # 4.a + b = target exists in a list
a=3
b=6
target=a+b
flag=False
list1=[2,6,7,4,9]
for i in list1:
    if i ==target:
        flag=True
       
if flag==True:
    print(target,"is in the list")
else:
    print("not there")

# =========================================================

# 3.subset or not
arr1 = [1, 23, 5, 3, 8, 9]
arr2 = [8, 7]
flag = True  
for j in arr2:
    found = False 
    for i in arr1:
        if i == j:
            found = True
            break
    if not found:  
        flag = False
        break

if flag:
    print("Subset")
else:
    print("Not a subset")

# ============================================================

# 1.list sorted or not

list2=[9,10,5,0]
status=True
if list2[0]<list2[len(list2)-1]:
    a=list2[0]
    
    for i in list2:
        
        if i>=a:
            a=i
            continue
        else:
            print("not sorted")
            status=False
            break
    if(status):
        print("Sorted in asc")
else:
    a=list2[len(list2)-1]
    for i in range(len(list2)-1,-1,-1):
        if list2[i]>=a:
            a=list2[i]
            continue
        else:
            print("not sorted")
            status=False
            break
    if(status):
        print("Sorted in desc")

# =======================================================================

# -- 2.missing number:--

#using formula:

list1=[1,2,4,5,6,7,8]
n=len(list1)+1
sum2=n*(n+1)//2
sum1=sum(list1)
miss_num=sum2-sum1
print(miss_num)

# -------------------------------------------

#using two loops:

list1 = [1, 2, 4, 5, 6, 7, 8]
miss_num = []


smallest = list1[0]
largest = list1[0]

for num in list1:
    if num < smallest:
        smallest = num
    if num > largest:
        largest = num

for i in range(smallest, largest + 1):
    found = False
    for j in list1:
        if i == j:
            found = True
            break
    if not found:
        miss_num.append(i)

print("missing num is:",miss_num)

# --------------------------------------------------------

#using xor method:

def find_missing_number(arr, n):
    xor_all = 0
    xor_arr = 0

    for i in range(1, n + 1):
        xor_all ^= i

    for num in arr:
        xor_arr ^= num

    return xor_all ^ xor_arr

list1 = [1, 2, 4, 5, 6, 7, 8]
n = 8  

missing_number = find_missing_number(list1, n)
print("Missing number:", missing_number)

# -----------------------------------------------------------------

#sorted method:

def find_missing_number(arr):
    arr.sort()  
    for i in range(len(arr)):
        if arr[i] != i + 1: 
            return i + 1
    return len(arr) + 1 


list1 = [1, 2, 4, 5, 6, 7, 8]

missing_number = find_missing_number(list1)
print("Missing number:", missing_number)













li=[1,2,3,45,23,45]
for i in li:
    print(f"the list elements are :{i}",)
print("*************************************************")

print(li[1])
print(len(li))
print("*************************************************")

li[2]=99
print(li[2])
print("*************************************************")

li.pop(3)
for i in li:
    print(i)
print("*************************************************")
li.remove(23)
for i in li:
    print(i)
print("*************************************************")

count=0
for i in li:
    count+=i
print(f"sum:{count}")
print("*************************************************")
n=len(li)
avg=count//n
print(f"average:{avg}")
print("*************************************************")


lis=[12,32,45,34,23,67,89,101,99]
max=0
for i in lis:
    if i>max:
        max=i
print(max)
print("*************************************************")
min=lis[0]
for i in lis:
    if i<min:
        min=i
print(min)
print("*************************************************")

li=[12,23,12,43,54,66,76]
even=0
odd=0
for i in li:
    if i%2==0:
        even=even+1
        print(f"the number is even:{i}")
    else:
        odd=odd+1
        print(f"the number is odd:{i}")
print(f"the total evens are {even}")
print(f"the total odd are {odd}")
print("*************************************************")

lis=[12,23,45,24,45,67,23,23]
count=0
for i in lis:
    if i==23:
        count=count+1
print(f"the total count is :{count}")
print("*************************************************")

lis=[12,23,45,24,45,67,23,23]
for i in range (0,len(lis),2):
    print(f"the elements at even indexes{lis[i]}")
for i in range (1,len(lis),2):
    print(f"the odd elements {lis[i]}")
print("*************************************************")


def liner(li,key):                      #liner search
    for i in range(len(li)):
        if li[i]==key:
            return i
    return False
li=[12,23,12,24,54,56,34,65]
key=int(input("enter the key:"))
result=liner(li,key)
print(result)
print("*************************************************")

def exist(li,element):           #element exist or not
    for i in li:
        if i==element:
            return True
        return -1
li=[23,34,233,45,46]
e=int(input("enter the element:"))
result=exist(li,e)
print(result)
print("*************************************************")

def fre(li,element):                    #frequency count
    count=0
    for i in range (len(li)):
        if li[i]==element:
            count=count+1
    return count
li=[12,23,43,56,34,23,23,23]
element=int( input("enter the element"))
result=fre(li,element)
print(result)
print("*************************************************")

li=[23,34,23,34,45,45,53]                   #duplicate elements
count=0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
             print(li[i])
print("*************************************************")

li=[12,13,22,44,56,12,22]                   #removing duplicates with out method
sceen={}
for i in li:
    if i not in sceen:
     sceen.append(i)
print(sceen)

n=3 
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    for j in range(n-i-1):
        print("*", end="")
    for k in range(i+1):
        print(" ", end="")
    print() 
print("*************************************************")
def twoSum(self, numbers, target):   
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l=0
        r=len(numbers)-1
        while l<r:
    
            if numbers[l]+numbers[r]== target:
                return[l+1,r+1]
            elif numbers[l]+numbers[r]<target:
                l=l+1
            else:
                r=r-1
print("*************************************************")
#User function Template for python3
def findMinDiff(self, arr, M):
        n = len(arr)
        if M == 0 or n == 0:
            return 0
        if M > n:
            return -1
        arr.sort()
        min_diff = float('inf')
        for i in range(n - M + 1):
            diff = arr[i + M - 1] - arr[i]
            min_diff = min(min_diff, diff)
        return min_diff
print("*************************************************")


def overlapInt(self, arr):
        # code here
        n = len(arr)
        start = sorted([i[0] for i in arr])
        end   = sorted([i[1] for i in arr])
        active =0
        i=j=0
        max_active=0
        while i < n and j < n:
                if start[i]<=end[j]:
                  active=active+1
                  max_active=max(max_active,active)
                  i=i+1
                else:
                    active =active- 1
                    j =j+ 1
        return max_active
print("***********************************************")   


def inversionCount(self, arr):
        # Code Here
        count=0
        n=len(arr)
        for i in range (n):
            for j in range(i+1,n):
                if arr[i]>arr[j]:
                    count=count+1
        return count
print
        
def missingRange(self, arr, low, high):
        #code here
        s=set(range(low,high+1))
        s2={x for x in arr if low<= x <= high}
        return sorted(s-s2)
print("*************************************************")


def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int(''.join(map(str, digits)))
        num += 1                              
        return list(map(int, str(num))) 


def hIndex(self, citations):
        #code here
        h=0
        citations.sort(reverse=True)
        for i in range(len(citations)):
            if citations[i]>=i+1:
                h=i+1
            else:
                break
        return h
#sub array

def subarrayXor(self, arr, k):
        # code here
        prefix_xor = 0
        count = 0
        freq = {0: 1}  

        for num in arr:
            prefix_xor ^= num
            need = prefix_xor ^ k
            count += freq.get(need, 0)
            freq[prefix_xor] = freq.get(prefix_xor, 0) + 1

        return count
print("*******************************************************")

'''union of a list'''  
def findUnion(self, a, b):
        # code here
        s=set(a+b)
        return list(s)
print("*******************************************************")


def removeDuplicates(self, nums):      #sorted array
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1  
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
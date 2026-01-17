def secound(li):                            #secound largest element
    max=0
    secmax=0
    for i in li:
        if i>max:
            secmax=max
            max=i
    return max,secmax
li=[1,12,14,48,52,2,3]
result=secound(li)
print(f"the two largest elements are:{result}")
print("*************************************************")

def binarysearch(li,key):                    #binary search
    start=0
    end=len(li)-1
    while start<end:
        mid=(start+end)//2
        if li[mid]==key:
            return mid
        elif li[mid]>key:
            end=mid-1
        else :
            start=mid+1
    return -1
li=[12,34,23,45,23,56,74]
li.sort()
key=int(input("enter search key:"))
print(binarysearch(li,key))
print("*************************************************")

def duplicates(li1,li2):                                     #duplicate in two elements
    result=[]
    for i in li1:
        for j in li2:
            if i==j and i  not in result:
             result.append(i)
    return result
li1=[2,3,1,4,5]
li2=[3,4,12,5,6]
print(f"the duplicates set is {duplicates(li1,li2)}")
print("*************************************************")


def dup(li):                                     #removing duplicates from list
 result=[]
 for i in li:
     if i not in result:
         result.append(i)
 return result
li=[1,2,3,4,3,2,1,5,6,7,5]
print(f"the list after removing duplicates is :{dup(li)}")
print("*************************************************")

li=[12,34,23,45,65,78,34]                     #reversing a list
rev=li[::-1]
print(f"the reversed list is :{rev}")



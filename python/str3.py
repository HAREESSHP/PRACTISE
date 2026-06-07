str="hii"
print(str.endswith("hi"))
print("*************************************************")

str="hello world"
print(str.replace("world","hello"))
print("*************************************************")

str=input("enter a string:")
li=str.split()
print(li)
lis=[]
for i in range(len(li)-1,-1,-1):
    lis.append(li[i])
print(lis)
print("*************************************************")

str=input("Enter the string:")                       #total substrings
n=len(str)
t=n*(n+1)//2
print(f"Total number of substrings are :{t}")
print("*************************************************")

str="abc"                                           #all substrings
sub=[]
for i in range(len(str)):
    for j in range(i+1,len(str)+1):
        sub.append(str[i:j])
        
print(sub)
print("*************************************************")


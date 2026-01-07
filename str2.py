import string
str="hareesh"
fre={}
for s in str:
    if s in fre:
        fre[s]+=1
    else:
        fre[s]=1
for key,value in fre.items():
    print(f"{key}:{value}")
print("*************************************************")

                               #panagram
s=input("Enter the string:")
character=set(string.ascii_lowercase)
s=s.lower()
sceen=set(s)
if character<=sceen:
    print("panagram")
else:
    print("no")
print("*************************************************")


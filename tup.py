t=(1,2,3,4,5)
print(t)
print(t[0])
print(t[-1])
print("**********************************")
print(t.count(2))
print(t.index(4))
print("*************************************")
a,b,c,d,e=t
print(a)
print(b)
print(c)
print(d)
print(e)
print("**********************************")

li=list(t)
print(li)
print("********************************")
t1=tuple(li)
print(t1)
print("********************************")

t2=(1,2,3,4,5)
print(t2)
print(t2[2])
print("********************************")
t3=t1+t2
print(t3)
lis=list(t3)
count=0
for i in lis:
    if i%2==0:
        count=count+1
print(f"even:{count}")
print("*****************************")
max=0
for i in lis:
    if i>max:
        max=i
print(max)
print
rev=[]
for i in range(len(lis)-1,-1,-1):
    rev.append(lis[i])
print(rev)
print("****************************")

sceen=set(t3)
print(sceen)
if sceen == t3:
    print("unique")
else:
    print("not unique")
print("***************************")
squares=tuple(i*i for i in range(1,11))
print(squares)
print("****************************")

    

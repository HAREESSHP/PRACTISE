li=[12,34,23,45,23,45]
sceen=set(li)
print(sceen)

li=[1,12,23,25,58,42,16]
sceen=set(li)
if li == sceen:
    print(True)
else:
    print(False)
print("-------------------")
li=[12,23,23,45,34,32]
sceen=set(li)
print(len(sceen))

li=[12,23,34,223,21,34]
s1=set(li)
list=[12,23,45,23]
s2=set(list)
print(s1&s2)

li=[12,23,34,223,21,34]
s1=set(li)
list=[12,23,45,23]
s2=set(list)
print(s1&s2)

s={1,2,3,4}                #basic set operations
print(s)
print(s.pop())
s.discard(4)
print(s)
s.add(5)
print(s)
li=[6,5,4,7,8,9]
s.update(li)
print(s)
#s.clear()
print(s)
s1={12,3,1,45,67,89}
s3=s|s1
print(s3)
s4=s^s1
print(s4)

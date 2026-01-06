li=[12,34,23,45,23,45]
sceen=set(li)
print(sceen)

li=[12,34,23,34,23]
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

m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
m1=[]
mr1=[]
mr2=[]
mr3=[]
print(m)
for j in range(0,len(m)):
 for i in range(len(m)):
        m1.append(m[i][j])
print(m1)
print("********************************")
for i in range (2,-1,-1):
    mr1.append(m1[i])
print(mr1)
for i in range (5,2,-1):
    mr2.append(m1[i])
print(mr2)
for i in range (8,5,-1):
    mr3.append(m1[i])
print(mr3)
print("********************************")

m=[                                                 #optimal solution
    [1,2,3],
    [4,5,6],
    [7,8,9]]
rotated=[]
n=3
print(m)
for j in range(n-1,-1,-1):
    row=[]
    for i in range (3):
        row.append(m[i][j])
    rotated.append(row)
print(rotated)
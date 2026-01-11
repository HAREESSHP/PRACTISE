m=[
    [1,2,3],
    [4,5,6],
    [7,8,9]]
print(m)
n=3
top=0
left=0
right=0
m1=[]
for i in range(left<3):
    for j in range(len(m)):
        m1.append(m[i][j])
        left=left+1
for j in range(len(m)):
 for i in range(1,len(m)):
     if i<j:
      m1.append(m[i][j])
for i in range(len(m)-1,right<4,-1):
    for j in range(len(m)-1,-1,-1):
     m1.append(m[i][j])
     right=right+1
     if i==0 and j==2:
         m1.append(m[i][j-1])
for i in range(1,len(m)):
    for j in range(len(m)):
       m1.append(m[i][j]) 
       top=top+1
       if top == 2 :
           stop=1
           break
    if stop == 1:
        break
print(m1)
        
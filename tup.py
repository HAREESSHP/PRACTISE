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

print("queue management system")
stack=[]
for i in range(0,10,1):
    s=input("enter person name")
    if i in range:
        stack.push(s)
    else:
        stack.pop()
        stack.push(s)
print("excectued sucessfully queue management system")
print("queque handling sucessfully")

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

def secound(li):                                     #second largest element in list
    max=0
    secmax=0
    for i in li:
        if i>max:
            secmax=max
            max=i
    return max,secmax

str="medem"
if str==str[::-1]:
    print("palindrome") 
else:
    print("not palindrome")

str1="hello world"

day = "may 4"
if day=="may 4":
    print("wish me happy birthday  to me")
else:
    print("today is not my birthday")

# stack
stack=[]
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)
stack.pop() 
print(stack)


# stack 
stack=[]
stack.append(1)
stack.append(2)
print(stack)
stack.delete(0)
print(stack)
stack.append(3)
print(stack)

def secinstack(s,key):
    for i in s:
        if i==key:
            print("key found ")

        else:
            print("not found")
    return -1
s=[1,3,4,2,6]
key=4
print(s,key)
print(secinstack(s,key))

#amstrong number
n=int(input("Enter a number:"))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**3
    temp//=10
print(f"{n} is an amstrong number") if n==sum else print(f"{n} is not an amstrong number")

#binary tree
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
class BinaryTree:
    def __init__(self):
        self.root=None
    def insert(self,data):
        if self.root is None:
            self.root=Node(data)
        else:
            self._insert(data,self.root)
    def _insert(self,data,node):
        if data<node.data:
            if node.left is None:
                node.left=Node(data)
            else:
                self._insert(data,node.left)
        else:
            if node.right is None:
                node.right=Node(data)
            else:
                self._insert(data,node.right)
    def inorder(self):
        self._inorder(self.root)    
    def _inorder(self,node):
        if node:
            self._inorder(node.left)
            print(node.data,end=' ')
            self._inorder(node.right)
bt=BinaryTree()
bt.insert(5) 
bt.inorder()
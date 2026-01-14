n=3                         #right star
for i in range(n):
    for j in range(i+1):
     print("*", end=" ")
    print()
print("program ended")
print("*************************************************")
n=3                         #left star
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
print()
print("*************************************************")
n=3                         #left star
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()
print("*************************************************")

n=3 
for i in range(n):
    for j in range(n-i-1):
        print(" ", end="")
    for k in range(i+1):
        print("*", end="")
    print() 
print("*************************************************")

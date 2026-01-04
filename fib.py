n=int(input("enter a number:")) #fibonacci series
n1=0
n2=1
if n<=0:
    print("please enter a positive integer")
elif n==1:
    print("fibonacci series:")
    print(n1)
else:
    print ("fibonacci series:")
    print(n1)
    print(n2)   
    for i in range(n-2):
                    n3=n1+n2
                    n1=n2
                    n2=n3
                    print (n3)                     

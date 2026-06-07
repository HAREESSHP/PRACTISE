def strrev(str):                 #reverse string
    str2=str[::-1]
    print(str2)
str=input("enter the string:")
strrev(str)
print("*************************************************")

def palin(str1,str2):                                  #palindrome
    if str1==str2:
        print("The strings are palindrome")
    else:
        print("The strings are not palindrome")
        
str1=input("Enter first string:")
str2=input("Enter secound string:")
palin(str1,str2)
print("*************************************************")

def vowelscount(str,vowels):                   #vowels count
    count=0
    for s in str:
        if s in vowels:
            count=count+1
            print(s)
    print(count)
str=input("Enter a string:")
v="aeiou"
vowelscount(str,v)
print("*************************************************")

def constcount(str,vowels):                    #consonants count       
    count=0
    for s in str:
        if s not in vowels:
            count=count+1
            print(s)
    print(count)
str=input("Enter a string:")
v="aeiou"
constcount(str,v)
print("*************************************************")


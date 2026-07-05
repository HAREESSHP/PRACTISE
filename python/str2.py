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

name=input("enter your name ")
print(name)


#unigue element of a string
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for ch in t:
            if ch not in freq or freq[ch]==0:
                return ch
            freq[ch]-=1


#is a substring
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>len(t):
            return False
        i=0
        for char in t:
            if i<len(s) and s[i]==char:
                i=i+1
        return i==len(s)
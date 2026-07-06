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

#first and last element
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        list=[-1,-1]
        def first(nums,target):
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid] == target:
                    ans= mid
                    r=r-1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        def last(nums,target):
            l=0
            r=len(nums)-1
            ans=-1
            while(l<=r):
                mid=(l+r)//2
                if nums[mid] == target:
                    ans= mid
                    l=mid+1
                elif nums[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return ans
        a=first(nums,target)
        b=last(nums,target)
        list[0]=a
        list[1]=b
        return list

#kadyens algo
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c=nums[0]
        m=nums[0]
        for i in range(1,len(nums)):
            c=max(nums[i],c+nums[i])
            m=max(m,c)
        return m
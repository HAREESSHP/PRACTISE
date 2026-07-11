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

#28
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)]==needle:
                return i
        return -1


#N queen problem
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag1 = set()     
        diag2 = set()    

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):

                if col in cols:
                    continue

                if (row - col) in diag1:
                    continue

                if (row + col) in diag2:
                    continue

                board[row][col] = "Q"
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)

                backtrack(row + 1)
                board[row][col] = "."
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)

        backtrack(0)
        return res

#height checker
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected=sorted(heights)
        count=0
        for i in range(len(heights)):
            if heights[i] != expected[i]:
                count=count+1
        return count

#biary addition
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a=int(a,2)
        b=int(b,2)
        result=bin(a+b)[2:]
        return result

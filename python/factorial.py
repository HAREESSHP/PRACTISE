n=int(input("Enter a number: ")) # factorial calculation
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
print("Factorial of", n, "is", factorial(n))


#left and ryt diff
def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        le=[0]*len(nums)
        re=[0]*len(nums)
        for i in range(1,len(nums)):
            le[i]=nums[i-1]+le[i-1]
        for i in range(len(nums)-2,-1,-1):
            re[i]=nums[i+1]+re[i+1]
        ans=[]
        for i in range(len(nums)):
            ans.append(abs(le[i]-re[i]))
        return ans

#Buddy string
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        if len(s)!=len(goal):
            return False
        if s==goal:
            return len(set(s))<len(s)
        ls=[]
        for i in range(len(s)):
            if s[i]!=goal[i]:
                ls.append(i)
        if len(ls)!=2:
            return False
        i,j=ls
        return s[i]==goal[j] and s[j]==goal[i]

#max product
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls=[]
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ls.append((nums[i]-1)*(nums[j]-1))
        return max(ls)

#smallest elements in an array
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans=[]
        for i in range(len(nums)):
            count=0
            for j in range(len(nums)):
                    if nums[i]>nums[j]:
                     count=count+1
            ans.append(count)
        return ans
#revrse array technique
    def canBeEqual(self, target, arr):
        """
        :type target: List[int]
        :type arr: List[int]
        :rtype: bool
        """
        target.sort()
        arr.sort()
        return target == arr

#Highest altitude
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ans=[0]
        for i in range(len(gain)):
            su=ans[i]+gain[i]
            ans.append(su)
        return max(ans)
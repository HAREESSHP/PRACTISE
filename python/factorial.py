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

        
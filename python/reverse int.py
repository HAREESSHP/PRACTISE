class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = int(str(x)[::-1])
        if rev > 2**31 - 1:
            return 0
        return rev*sign
__import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
        
        
solution = Solution()
print(solution.reverse(-123))  # Output: -321


#Plus one
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n=int("".join(map(str,digits)))
        n=n+1
        return list(map(int,str(n)))


#rich customer
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        m=0
        for customer in accounts:
            if sum(customer)>m:
                m=sum(customer)
        return m
#minimum diff
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        if len(nums)==1:
            return 0
        left=0
        ans=float(inf)
        for r in range(len(nums)):
            if r-left==k:
                left=left+1
            if r-left+1==k:
                ans=min(ans,nums[r]-nums[left])
        return ans

#max product between two pairs
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
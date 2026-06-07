class Solution(object):
    def canPartition(self, nums):
        total = sum(nums)
        
        if total % 2 != 0:
            return False
        
        target = total // 2
        possible = set([0])
        
        for num in nums:
            new_possible = set()
            for s in possible:
                if s + num == target:
                    return True
                if s + num < target:
                    new_possible.add(s + num)
            possible |= new_possible
        
        return target in possible

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left=0
        mid = 0
        right=len(nums)-1
        while(mid<=right):
            if nums[mid]==0:
                nums[left],nums[mid]=nums[mid],nums[left]
                left=left+1
                mid=mid+1
            elif nums[mid]==1:
                mid=mid+1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
        return nums
#matrix diagonal sum
class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        sum=0
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i==j:
                    sum=sum+mat[i][j]
        for i in range(len(mat)):
            for j in range(len(mat)):
                if i+j==len(mat)-1:
                    sum=sum+mat[i][j]
        if len(mat) % 2 == 1:
            k=len(mat)//2
            sum=sum-mat[k][k]
        return sum
obj=Solution()
mat={
    [1,2,3],
    [4,5,6],
    [7,8,9]
}
result=obj.diagonalSum(mat)
print(result)
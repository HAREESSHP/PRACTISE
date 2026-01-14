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

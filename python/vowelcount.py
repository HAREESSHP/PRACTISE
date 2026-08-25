s="hi im a good boy"
s.lower()
li=[]
vowel_count=0
for i in s:
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        li.append(i)
        vowel_count+=1
print(vowel_count)
print(li)

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        s=[]
        current=head
        while current is not None:
            s.append(current)
            current=current.next
        n=len(s)//2
        return s[n]
        

class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        if k == 1:
            count = Counter(nums)
            ans = -1

            for x in nums:
                if count[x] == 1:
                    ans = max(ans, x)
            return ans
        if k == n:
            return max(nums)
        count = Counter(nums)
        ans = -1
        if count[nums[0]] == 1:
            ans = max(ans, nums[0])

        if count[nums[-1]] == 1:
            ans = max(ans, nums[-1])

        return ans

#attendence 1
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        absent = 0
        late = 0

        for ch in s:
            if ch == 'A':
                absent += 1
                late = 0
            elif ch == 'L':
                late += 1
            else:
                late = 0

            if absent >= 2 or late >= 3:
                return False
        return True

#Digit sum and product problem
    def checkDivisibility(self, n):
        """
        :type n: int
        :rtype: bool
        """
        p=1
        s=0
        x=n
        while x>0:
            digit=x%10
            s+=digit
            p*=digit
            x=x//10
        return n%(s+p)==0

#smalest multiple missing
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        s = k
        while s in nums:
            s += k
        return s
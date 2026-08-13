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
        
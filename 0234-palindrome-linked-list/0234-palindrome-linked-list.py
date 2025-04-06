# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # my idea: reverse the second part and then compare
        # another idea is to use stack

        stack = []
        cur = head
        while cur:
            stack.append(cur.val)
            cur = cur.next
        
        cur = head
        while cur and stack: 
            reverseEle = stack.pop()
            if cur.val != reverseEle: 
                return False
            cur = cur.next
        
        return not stack


        
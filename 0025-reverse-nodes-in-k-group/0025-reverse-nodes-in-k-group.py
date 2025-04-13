# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # My idea: we treat group as the entire linkedlist and then each time iterate k length
        def reverseLinkedList(start, end): # start is the parent node of the 1, end is 3 so basically [start, end]
            # 做错的点：一直卡在这个while判断这里，说是 cur！= end.next 这里是因为end.next 在变化，所以需要提前保存end.next
            stop = end.next
            prev = end.next
            cur = start 
            while cur != stop:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            return end, start

        
        dummy = ListNode()
        dummy.next = head
        cur = dummy
        
        while True:
            count = 0
            start = cur.next
            end = cur

            while count < k and end.next:
                end = end.next
                count += 1
            
            if count < k:
                break
            
            next_group_start = end.next
            new_head, new_tail = reverseLinkedList(start, end)
            
            cur.next = new_head
            new_tail.next = next_group_start
            
            cur = new_tail
        return dummy.next

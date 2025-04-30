# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy

        while any(node is not None for node in lists):   # 只要还有没走完的链表
            min_val = float('inf')
            min_idx = -1

            for i in range(len(lists)):
                if lists[i] and lists[i].val < min_val:  # 找当前最小表头节点
                    min_val = lists[i].val
                    min_idx = i

            if min_idx == -1:  # 安全性判断（应该不会触发）
                break

            cur.next = lists[min_idx]          # 接到结果链表
            cur = cur.next                     # cur 往后走
            lists[min_idx] = lists[min_idx].next  # 原链表向前推进一位

        return dummy.next

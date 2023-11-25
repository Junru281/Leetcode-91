# Leetcode 142  #

[142. Linked List Cycle II](https://leetcode.cn/problems/linked-list-cycle-ii/)

**Ideas**

由于昨天的Leetcode题目与此题类似, 所以非常容易想到用HashSet来储存已经遍历的node, 下一次如果出现同样的node, 即为cycle的开头.

```java
/**
 * Definition for singly-linked list.
 * class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public ListNode detectCycle(ListNode head) {
        ListNode tmp = head;
        HashSet<ListNode> visited = new HashSet<>();
        while(tmp != null){
            if(visited.contains(tmp.next)){
                return tmp.next;
            }
            visited.add(tmp);
            tmp = tmp.next;
        }
        return null;
        
    }
}
```

**Mistakes**

在写的时候注意到了edge case, 但是重复考虑了. 本身while的condition就可以handle了.

**Complexity**

Time Complexity: O(n) # loop though every element in the LinkedList 
Space Complexity: O(n) # at most store all the elements in the LinkedList


**Improvment**

提示可以使用双指针, 即快慢指针, 但我写的时候没想明白为什么他们相遇的地方会是环的入口. 

# Leetcode 232 Nov 20 #
[232. Implement Queue using Stacks](https://leetcode.cn/problems/implement-queue-using-stacks/)

**Ideas**

The huge difference between a stack and a queue is the order to retrieve an element. 
By the hint that we are going to us e two stack, we can use one stack to store elements just as queue and use the other stack to reverse the order of one queue.
In other words, before we push the new element, we first pop all existing elements and then push the new element to the bottom of a stack. Then push all the element back, 
so that the first element is still at the top of the stack. 

```java
class MyQueue {
    Stack<Integer> queue;
    Stack<Integer> records;

    public MyQueue() {
        queue = new Stack<>();
        records = new Stack<>();
    }
    
    public void push(int x) {
        while(!queue.empty()){
            int top_queue = queue.pop();
            records.push(top_queue);
        }
        queue.push(x);
        while(!records.empty()){
            int next = records.pop();
            queue.push(next);
        }
    }
    
    public int pop() {
        return queue.pop();
    }
    
    public int peek() {
        return queue.peek();
    }
    
    public boolean empty() {
        if(queue.empty()){
            return true;
        }
        else return false;
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
```

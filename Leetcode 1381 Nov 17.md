# Leetcode 1381 Nov 17

[1381. Design a Stack With Increment Operation](https://leetcode.cn/problems/design-a-stack-with-increment-operation/)

**Ideas:** 

Stack can be represented as an array "standing up" with its top and bottom. Therefore, we use the array to replace the stack.  

```java
class CustomStack {
    int[] stack;
  	// pointer here represents the current element
    int pointer = -1;
  	// create the stack frame by initialzie an array of size (maxsize)
    public CustomStack(int maxSize) {
        stack = new int[maxSize];
    }
    //remember to check if the array is out of space
    public void push(int x) {
        if(pointer + 1 <= stack.length-1){
            stack[pointer+1] = x;
            pointer ++;
        }
    }
    // remember to check if the stack frame is still null --> pointer is -1
    public int pop() {
        if(pointer == -1){
             return -1;
        }
        int ret_val = stack[pointer];
        pointer --;
        return ret_val;
    }
    //  first to find the correct number of elements to update
  	//  then use a for loop to update all "k" value
    public void increment(int k, int val) {
        int min_count = Math.min(pointer, k-1);
        for(int i = 0; i<=min_count; i++){
                stack[i] = stack[i]+val;
        }
    }
}

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack obj = new CustomStack(maxSize);
 * obj.push(x);
 * int param_2 = obj.pop();
 * obj.increment(k,val);
 */
```


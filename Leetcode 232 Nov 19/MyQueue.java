import java.util.Stack;

public class MyQueue {
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
        if(queue.empty())
            return -1;
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


/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */
}

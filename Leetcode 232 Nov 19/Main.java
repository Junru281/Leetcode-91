public class Main {
    public static void main(String[] args) {
        // ["MyQueue","push","push","push","push","pop","push","pop","pop","pop","pop"]
        // [[],[1],[2],[3],[4],[],[5],[],[],[],[]]
        MyQueue obj = new MyQueue();
        obj.push(1);
        obj.push(2);
        obj.push(3);
        obj.push(4);
        System.out.println(obj.pop());
        obj.push(5);
        System.out.println(obj.pop());
        System.out.println(obj.pop());
        System.out.println(obj.pop());
        System.out.println(obj.pop());

    }
}

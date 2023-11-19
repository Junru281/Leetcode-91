import java.util.Stack;

class Solution {
    public static String decodeString(String s) {
        Stack<String> stack = new Stack<>();
        int times = 0;
        int left_ptr = 0;
        int right_ptr = -1;
        while(s.contains("[")) {
            String rep = "";
            int num_start = 0;
            for (int i = 0; i < s.length(); i++) {
                if(Character.isDigit(s.charAt(i))){
                    num_start ++;
                }
                if (s.charAt(i) == '[') {
                    times = Integer.parseInt(s.substring(i-num_start, i));
                    left_ptr = i-num_start;

                    for (int j = i + 1; j < s.length(); j++) {
                        stack.push(s.substring(j, j + 1));
                        if(Character.isDigit(s.charAt(j))){
                            if(!Character.isDigit((s.charAt(j-1)))){
                                num_start = 0;
                            }
                            num_start ++;
                        }
                        if (s.charAt(j) == '[') {
                            stack.clear();
                            left_ptr = j-num_start;
                            times = Integer.parseInt(s.substring(j-num_start, j));
                        }
                        if (s.charAt(j) == ']') {
                            stack.pop();
                            right_ptr = j;
                            break;
                        }
                    }

                    while (!stack.isEmpty()) {
                        rep = stack.pop() + rep;
                    }

                    String tmp = rep;
                    for (int m = 0; m < times - 1; m++) {

                        rep = rep + tmp;
                    }

                    s = s.substring(0, left_ptr) + rep + s.substring(right_ptr + 1);

                    break;
                }
            }

        }
        return s;

    }


    public static void main(String[] args) {
        System.out.println(decodeString("3[a10[bc]]"));

    }
}


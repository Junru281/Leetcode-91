# Leetcode 394 Nov 19 #

[394. Decode String](https://leetcode.cn/problems/decode-string/)

**Ideas**

Contact with bracket matching problem, so stack is used

The main problem was how to extract the number, and I finally used a separate parameter to record it. But it took some time to figure out when to clear it to zero and add 1. 


```java
class Solution {
    public String decodeString(String s) {
Stack<String> stack = new Stack<>();
        int times;
        int left_ptr;
        int right_ptr = 0;
        while(s.contains("[")) {
            String rep = "";
            for (int i = 0; i < s.length(); i++) {
                if (s.charAt(i) == '[') {
                    times = Integer.parseInt(s.substring(i - 1, i));
                    left_ptr = i - 1;
                    for (int j = i + 1; j < s.length(); j++) {
                        stack.push(s.substring(j, j + 1));
                        if (s.charAt(j) == '[') {
                            stack.clear();
                            times = Integer.parseInt(s.substring(j - 1, j));
                            left_ptr = j - 1;
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
}
```

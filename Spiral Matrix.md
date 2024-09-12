## Sept 12 Leetcode Daily Challenge
### 54 Spiral Matrix
https://leetcode.cn/problems/spiral-matrix/
```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        if matrix == None or len(matrix) == 0 or len(matrix[0]) == 0:
            return ans

        # 这里是上下左右的边界
        left = 0
        top = 0
        bottom = len(matrix) - 1
        right = len(matrix[0]) - 1

        while True:
            for i in range(left, right + 1):
                ans.append(matrix[top][i])

            top += 1
            if top > bottom:
                break

            for i in range(top, bottom + 1):
                ans.append(matrix[i][right])

            right -= 1
            if right < left:
                break

            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1
            if bottom < top:
                break

            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])
            left += 1
            if left > right:
                break

        return ans
```

See the question as a layer

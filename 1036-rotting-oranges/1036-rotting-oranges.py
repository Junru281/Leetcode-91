class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # this is a bfs question 多源bfs问题
        # we can first calculate the number of fresh orange and then start from them
        res = 0
        fresh = 0
        m, n = len(grid), len(grid[0])
        queue = deque([])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while queue: 
            length = len(queue)
            for _ in range(length):
                i, j = queue.popleft()
                for dx, dy in directions: 
                    nx, ny = dx + i, dy + j
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1: 
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh -= 1
            res += 1

        return max(res - 1, 0) if fresh == 0 else -1

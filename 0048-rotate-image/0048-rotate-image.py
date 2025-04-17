class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        l, r = 0, n -1
        top, bottom = 0, n-1
        saveValues = []

        for i in range(l,r+1):
            saveValues.append(matrix[i][r])
            matrix[i][r] = matrix[top][i]
        r -= 1
        print(saveValues)

                
        
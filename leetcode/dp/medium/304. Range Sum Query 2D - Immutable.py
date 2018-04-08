__author__ = 'Hk4Fun'
__date__ = '2018/4/8 12:43'
'''题目描述：
Given a 2D matrix matrix, find the sum of the elements inside the rectangle 
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]

sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12
Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
'''
'''主要思路：
https://leetcode.com/problems/range-sum-query-2d-immutable/solution/
初始化O(mn),查询O(1),空间O(mn)

在构造函数中算出每个以(i,j)为右下角的矩阵的和，
计算每个矩阵总和时有：sums[i][j]=matrix[i-1][j-1]+sums[i][j-1]+sums[i-1][j]-sums[i-1][j-1]
而查询某个矩阵总和时有：sums[row2][col2]-sums[row2][col1-1]-sums[row1-1][col2]+sums[row1-1][col1-1]
'''


class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.sums = [[]]
            return
        rows, cols = len(matrix), len(matrix[0])
        self.sums = [[0] * (cols + 1) for _ in range(rows + 1)]  # 为方便计算，多出一行一列填充0
        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                self.sums[i][j] = matrix[i - 1][j - 1] + self.sums[i][j - 1] \
                                  + self.sums[i - 1][j] - self.sums[i - 1][j - 1]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.sums: return 0
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1
        return self.sums[row2][col2] - self.sums[row2][col1 - 1] \
               - self.sums[row1 - 1][col2] + self.sums[row1 - 1][col1 - 1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

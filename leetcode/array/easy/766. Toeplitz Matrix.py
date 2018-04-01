__author__ = 'Hk4Fun'
__date__ = '2018/4/1 18:40'
'''题目描述：
A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
Now given an M x N matrix, return True if and only if the matrix is Toeplitz.

Example 1:
Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512
In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]", 
and in each diagonal all elements are the same, so the answer is True.

Example 2:
Input: matrix = [[1,2],[2,2]]
Output: False
Explanation:
The diagonal "[1, 2]" has different elements.

Note:
matrix will be a 2D array of integers.
matrix will have a number of rows and columns in range [1, 20].
matrix[i][j] will be integers in range [0, 99].
'''
'''主要思路：
时间O（n^2），空间O（1）
思路1：检查每个对角线是否每个数都相等
思路2：遍历数组（最右边和最下边除外），检查每个数与右下角的数是否相等

明显思路2更快更简洁
'''


class Solution:
    """
    :type matrix: List[List[int]]
    :rtype: bool
    """

    def isToeplitzMatrix1(self, matrix):
        rows = len(matrix)
        cols = len(matrix[0])
        for _ in range(rows):  # 从最左边出发
            i = _
            j = 0
            while i < rows - 1 and j < cols - 1:
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                i += 1
                j += 1
        for _ in range(1, cols):  # 从最上边出发
            i = 0
            j = _
            while i < rows - 1 and j < cols - 1:
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
                i += 1
                j += 1
        return True

    def isToeplitzMatrix2(self, matrix):
        for i in range(len(matrix) - 1):  # 最右边除外
            for j in range(len(matrix[0]) - 1):  # 最下边除外
                if matrix[i][j] != matrix[i + 1][j + 1]:
                    return False
        return True


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[[1, 2, 3, 4], [5, 1, 2, 3], [9, 5, 1, 2]], True])
        testArgs.append([[[1, 2], [2, 2]], False])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

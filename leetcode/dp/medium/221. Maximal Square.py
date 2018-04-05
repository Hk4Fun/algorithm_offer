__author__ = 'Hk4Fun'
__date__ = '2018/4/4 22:17'
'''题目描述：
Given a 2D binary matrix filled with 0's and 1's, 
find the largest square containing only 1's and return its area.
For example, given the following matrix:
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.
'''
'''主要思路：
时间O（n^2），空间O（n）
一道非常典型的dp：http://www.cnblogs.com/jcliBlogger/p/4548751.html
状态转移方程：
P[i][j]表示以(i,j)为右下角的最大正方形的边长
P[0][j] = matrix[0][j] (topmost row);
P[i][0] = matrix[i][0] (leftmost column);
For i > 0 and j > 0: 
if matrix[i][j] = 0, P[i][j] = 0; 
if matrix[i][j] = 1, P[i][j] = min(P[i - 1][j], P[i][j - 1], P[i - 1][j - 1]) + 1.

空间上的优化可以二维优化成一维，一维需要两行，
但实际上只需要一行加一个变量pre即可，而对于这道题来讲，
可以把这个pre也省了，因为对于P[i - 1][j - 1]，
只需看matrix[i - k][j - k]是否为1即可判断该正方形能否形成，这可以直接从原矩阵中获取，
不必用pre，这里的k=min(P[i - 1][j], P[i][j - 1])
'''


class Solution:
    """
    :type matrix: List[List[str]]
    :rtype: int
    """

    def maximalSquare1(self, matrix):  # 一行加一个变量pre
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols
        maxLen = 1 if sum(dp) > 0 else 0
        for i in range(0, rows):
            for j in range(0, cols):
                tmp = dp[j]
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[j] = int(matrix[i][j])
                    else:
                        dp[j] = min(dp[j], dp[j - 1], pre) + 1
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
                pre = tmp
        return maxLen * maxLen

    def maximalSquare2(self, matrix):  # 一行，不用pre
        if not matrix: return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [0] * cols
        maxLen = 1 if sum(dp) > 0 else 0
        for i in range(0, rows):
            for j in range(0, cols):
                if matrix[i][j] == '1':
                    if j == 0:
                        dp[j] = int(matrix[i][j])
                    else:
                        k = min(dp[j], dp[j - 1])
                        dp[j] = (k + 1) if matrix[i - k][j - k] == '1' else k
                    maxLen = max(maxLen, dp[j])
                else:
                    dp[j] = 0
        return maxLen * maxLen


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        matrix = [["1", "0", "1", "0"], ["1", "0", "1", "1"], ["1", "0", "1", "1"], ["1", "1", "1", "1"]]
        testArgs.append([matrix, 4])

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

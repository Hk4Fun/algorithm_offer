__author__ = 'Hk4Fun'
__date__ = '2018/4/3 11:49'
'''题目描述：
Given a m x n grid filled with non-negative numbers, 
find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.
'''
'''主要思路：
时间O（m*n），空间O（n），空间可以优化成O（min（m,n）)
'''


class Solution:
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def minPathSum1(self, grid):
        dp = [float('inf')] * len(grid[0])
        dp[0] = 0
        for i in range(len(grid)):
            dp[0] += grid[i][0]
            for j in range(1, len(grid[0])):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        return dp[-1]

    def minPathSum2(self, grid):
        rows, cols = len(grid), len(grid[0])
        more, less = max(rows, cols), min(rows, cols)
        row_more = (more == rows)
        dp = [float('inf')] * less
        dp[0] = 0
        for i in range(more):
            dp[0] += (grid[i][0] if row_more else grid[0][i])
            for j in range(1, less):
                dp[j] = min(dp[j], dp[j - 1]) + (grid[i][j] if row_more else grid[j][i])
        return dp[-1]


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

        matrix = [[1, 3, 1],
                  [1, 5, 1],
                  [4, 2, 1]]
        testArgs.append([matrix, 7])

        testArgs.append([[[1, 2, 5], [3, 2, 1]], 6])

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

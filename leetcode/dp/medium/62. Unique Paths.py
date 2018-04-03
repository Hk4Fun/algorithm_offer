__author__ = 'Hk4Fun'
__date__ = '2018/4/3 1:23'
'''题目描述：
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
How many possible unique paths are there?

Note: m and n will be at most 100.
'''
'''主要思路：
思路1（时间O（n*m），空间O（n））:
到达某点的路径数等于到达该点上方的路径数加上该点左方的路径数
dp[i][j] = dp[i][j-1] + dp[i-1][j]
base case：dp[i][0] = dp[0][j] = 1
只和上方和左方有关，空间可以优化成O(n)

思路2（时间O（min(m,n)），空间O（1））:
可以看成是一道组合问题：
总共向右走n-1步R，向下走m-1步D，这所有的步骤进行组合就是总的路径数：
设m=m-1,n=n-1,则res = C(m,m+n) = (m+n)!/(m!n!)
'''

from math import factorial


class Solution:
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [1] * n  # 顺便把边界值给填了
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]

    def uniquePaths2(self, m, n):
        if m == 1 or n == 1: return 1
        n -= 1
        m -= 1
        if m < n: m, n = n, m
        res = j = 1
        for i in range(m + 1, m + n + 1):
            res *= i
            res /= j
            j += 1
        return int(res)

    def uniquePaths3(self, m, n):
        # 使用内置函数factorial计算阶乘
        return factorial(m + n - 2) // (factorial(m - 1) * factorial(n - 1))


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

        testArgs.append([3,3,6])
        testArgs.append([2,3,3])
        testArgs.append([1,10,1])
        testArgs.append([10,1,1])
        testArgs.append([4,4,20])

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

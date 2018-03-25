__author__ = 'Hk4Fun'
__date__ = '2018/3/25 12:32'
'''题目描述：
有一个机器人的位于一个 m × n 个网格左上角。
机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。
问有多少条不同的路径？
'''
'''主要思路：
动态规划：
到达某点的路径数等于到达该点上方的路径数加上该点左方的路径数
'''


class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        dp = [None] * n
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 : # 边界值
                    dp[j] = 1
                else:
                    dp[j] += dp[j-1]
        return dp[-1]


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
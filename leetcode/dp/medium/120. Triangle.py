__author__ = 'Hk4Fun'
__date__ = '2018/4/3 22:30'
'''题目描述：
Given a triangle, find the minimum path sum from top to bottom. 
Each step you may move to adjacent numbers on the row below.
For example, given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, 
where n is the total number of rows in the triangle.
'''
'''主要思路：
时间O（N），空间O（n）   (N--数据量，n--行数)
矿工问题，自底向上，dp[i][j]表示以第i层第j个数作为（自底向上）路径结尾的最小花费
则dp[k][i] = min(dp[k+1][i], dp[k+1][i+1]) + triangle[k][i]
base case：最后一层的花费（路径开头）等于自身
空间优化，一维数组即可
'''

from functools import reduce  # py3已经把reduce从内置函数中移除了


class Solution:
    """
    :type triangle: List[List[int]]
    :rtype: int
    """

    def minimumTotal1(self, triangle):
        dp = triangle[-1][:]
        for layer in range(len(triangle) - 2, -1, -1):
            for i in range(layer + 1):
                dp[i] = min(dp[i], dp[i + 1]) + triangle[layer][i]
        return dp[0]

    def minimumTotal2(self, triangle):  # 又是一行。。。
        return reduce(lambda a, b: [min(a[i], a[i + 1]) + n for i, n in enumerate(b)], triangle[::-1])[0]


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

        matrix = [
            [2],
            [3, 4],
            [6, 5, 7],
            [4, 1, 8, 3]
        ]
        testArgs.append([matrix, 11])

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

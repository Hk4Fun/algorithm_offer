__author__ = 'Hk4Fun'
__date__ = '2018/4/3 1:28'
'''题目描述：
Follow up for "Unique Paths":
Now consider if some obstacles are added to the grids. How many unique paths would there be?
An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
'''主要思路：
时间O（n*m），空间O（n）
'''


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [0] * n  # 这里先填充了0，这样当i==0时也可以dp[j] += dp[j-1]
        dp[0] = 1  # 左上角总是为1，也为后面i!=0而j==0的情况做铺垫
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:  # 遇到障碍物直接为0
                    dp[j] = 0
                elif j > 0:  # 没有遇到障碍物。因为j==0时，应该为dp[j] += 0，等于不变，所以略过
                    dp[j] += dp[j - 1]
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

        testArgs.append([[[0, 0], [0, 0], [0, 0], [1, 0], [0, 0]], 3])
        testArgs.append([[[0, 0, 0], [0, 1, 0], [0, 0, 0]], 2])

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

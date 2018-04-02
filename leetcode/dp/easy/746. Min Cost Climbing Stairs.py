__author__ = 'Hk4Fun'
__date__ = '2018/4/1 17:28'
'''题目描述：
On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
Once you pay the cost, you can either climb one or two steps. 
You need to find minimum cost to reach the top of the floor, 
and you can either start from the step with index 0, or the step with index 1.

Example 1:
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.

Example 2:
Input: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
Output: 6
Explanation: Cheapest is start on cost[0], and only step on 1s, skipping cost[3].

Note:
cost will have a length in the range [2, 1000].
Every cost[i] will be an integer in the range [0, 999].
'''
'''主要思路：
时间O（n），空间O（1）
动态规划：
1、正向理解：设f[i]为从第0阶出发到达第i阶的最少花费，则f[i] = cost[i] + min(f[i-1], f[i-2])
表示想要到达第i阶，要么从第i-1阶跳一层，要么从第i-2阶跳两层，则中间选最少的花费，加上本层的花费
边界条件：f[0] = cost[0], f[1] = cost[1]

2、反向理解：设f[i]为从第i阶出发到达顶层的最少花费，则 f[i] = cost[i] + min(f[i+1], f[i+2])
表示从第i阶出发要么跳一层，来到第i+1层，本层花费加上第i+1层到达顶层的花费；
要么跳两层，来到第i+2层，本层花费加上第i+2层到达顶层的花费；
二者中选最小的花费
边界条件：f[n] = cost[n], f[n-1] = cost[n-1]
'''


class Solution:
    """
    :type cost: List[int]
    :rtype: int
    """

    def minCostClimbingStairs_reverse(self, cost):
        f1, f2 = cost[-1], cost[-2]
        for x in cost[-3::-1]:
            f1, f2 = f2, x + min(f1, f2)
        return min(f1, f2)

    def minCostClimbingStairs_forward(self, cost):
        f1, f2 = cost[0], cost[1]
        for x in cost[2:]:
            f1, f2 = f2, x + min(f1, f2)
        return min(f1, f2)


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

        testArgs.append([[10, 15, 20], 15])
        testArgs.append([[1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6])

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

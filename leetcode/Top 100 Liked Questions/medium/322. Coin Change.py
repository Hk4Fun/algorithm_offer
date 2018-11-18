__author__ = 'Hk4Fun'
__date__ = '2018/8/21 19:41'
'''题目描述：
You are given coins of different denominations 
and a total amount of money amount. 
Write a function to compute the fewest number of coins 
that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''
'''主要思路：
设硬币种类个数为n
思路1（时间O（n*amount），空间O（amount））：
dp：https://leetcode.com/problems/coin-change/solution/
Approach #3 (Dynamic programming - Bottom up) 
https://ws1.sinaimg.cn/large/006giLD5ly1fxcbfzt70rj30hl0dv0ui.jpg

思路2：
上面的思路在oj上TLE了，采用 bfs 试一下：
https://ws1.sinaimg.cn/large/006giLD5ly1fxcbtc7etwj30s90a876j.jpg
利用该思路，如果题目要求每种面额的硬币只有一个，那么不难画出对应的分支树
'''


class Solution:
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """

    def coinChange1(self, coins, amount):
        dp = [0] + [float('inf')] * amount
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:  # 硬币面额不能超过目标金额，因为不能找零，保证 dp[i - c] 不越界
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange2(self, coins, amount):
        level = seen = {0}
        count = 0
        while level:
            if amount in level: return count
            # seen表示之前出现过的金额，在level中剪枝，表示可以用更少的硬币来获取该金额，不必继续累加
            level = {a + c for a in level for c in coins if a + c <= amount} - seen
            seen |= level
            count += 1
        return -1


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

__author__ = 'Hk4Fun'
__date__ = '2018/4/8 15:00'
'''题目描述：
Say you have an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times) with the following restrictions:
You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

Example:
prices = [1, 2, 3, 0, 2]
maxProfit = 3
transactions = [buy, sell, cooldown, buy, sell]
'''
'''主要思路：
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
时间O（n），空间O（1）
画出状态转移图：http://ox186n2j0.bkt.clouddn.com/%E8%BD%AC%E7%A7%BB%E5%9B%BE.png， 则有状态转移方程：
s0[i] = max(s0[i - 1], s2[i - 1]); // 停留在s0或者来自s2的rest
s1[i] = max(s1[i - 1], s0[i - 1] - prices[i]); // 停留在s1，或者来自s0的buy
s2[i] = s1[i - 1] + prices[i]; // 来自s1的sell
初始化：
s0[0] = 0; // 一开始就休息，则利润为0
s1[0] = -prices[0]; // 一开始就买了第一支股票，利润为负
s2[0] = 0; // 一开始不可能就买股票，所以该值无意义，0或者-float('inf')都行
最终利润最大值只能是s0[n]或者s2[n]，不可能来自s1[n]，
因为不可能在最后以买进股票结束而获取最大利润，这种情况下完全可以直接休息而不买任何股票来获取最大利润
可以空间优化，O(n)-->O(1)
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices: return 0
        s0, s1, s2 = 0, -prices[0], 0
        for i in range(1, len(prices)):
            last_s2 = s2
            s2 = s1 + prices[i]
            s1 = max(s1, s0 - prices[i])
            s0 = max(s0, last_s2)
        return max(s0, s2)


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

        testArgs.append([[1, 2, 3, 0, 2], 3])

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

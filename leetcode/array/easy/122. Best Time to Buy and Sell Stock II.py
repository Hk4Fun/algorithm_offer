__author__ = 'Hk4Fun'
__date__ = '2018/3/25 13:14'
'''题目描述：
Say you have an array for which the i^th element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(ie, buy one and sell one share of the stock multiple times). 
However, you may not engage in multiple transactions at the same time 
(ie, you must sell the stock before you buy again).
'''
'''主要思路：
时间O（n），空间O（1）
上一题只允许买入卖出最多发生一次，只能赚取一次最大差价；
而这一题允许多次买入卖出，这意味着我们可以多次从股票的差价中赚取利润：
如果明天股票会涨，那么今天就买入；如果明天股票会跌，那么今天就卖出。
注意：买入的时候若已经买过就不用再买了，可以理解为当天卖出再买入，相当于没卖
（买入的时候若已经买过说明股票一直在涨）
其核心就是：sum(每个波峰-左边相邻的波谷)
'''


class Solution:
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxProfit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                maxProfit += prices[i] - prices[i - 1]
        return maxProfit

    def maxProfit2(self, prices):  # pythonic
        return sum(max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices)))


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

        testArgs.append([[1, 7, 2, 3, 6, 7, 6, 7], 12])

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

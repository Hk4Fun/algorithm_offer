__author__ = 'Hk4Fun'
__date__ = '2018/3/25 12:47'
'''题目描述：
Say you have an array for which the i^th element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Example 1:
Input: [7, 1, 5, 3, 6, 4]
Output: 5
max. difference = 6-1 = 5 (not 7-1 = 6, as selling price needs to be larger than buying price)

Example 2:
Input: [7, 6, 4, 3, 1]
Output: 0
In this case, no transaction is done, i.e. max profit = 0.
'''
'''主要思路：
时间O（n），空间O（1）
target_offer补充73_股票的最大利润，思路一样，但这里提供更加简洁的代码：
由左至右遍历，总是获取当前的最小价格（包括当前值），
算出当前价格与当前最小价格的差价（利润）并保存最大利润
注意：当亏损时不买不卖，利润为0
'''


class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # 设置两个变量分别记录最小价格和最大利润
        maxProfit, minPrice = 0, float('inf')  # 设maxProfit为0可以保证出现负利润时返回0
        for price in prices:
            minPrice = min(minPrice, price)  # 看一下目前有没有更低的价格来买入
            profit = price - minPrice  # 假如现在卖出能赚多少钱
            maxProfit = max(maxProfit, profit)  # 记录下最大利润，以便后面作参考比较
        return maxProfit


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

        testArgs.append([[4, 1, 3, 2, 5], 4])
        testArgs.append([[1, 2, 4, 7, 11, 16], 15])  # 价格递增
        testArgs.append([[16, 11, 7, 4, 2, 1], 0])  # 价格递减
        testArgs.append([[16, 16, 16, 16, 16], 0])  # 价格全部相同
        testArgs.append([[9, 11, 5, 7, 16, 1, 4, 2], 11])
        testArgs.append([[2, 4], 2])
        testArgs.append([[4, 2], 0])
        testArgs.append([[1], 0])

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

__author__ = 'Hk4Fun'
__date__ = '2018/3/6 14:31'

'''题目描述：
假设把某股票的价格按照时间先后顺序存储在数组中，
请问买卖交易该股票可能获得的最大利润是多少？
例如一只股票在某些时间节点的价格为{9, 11, 8, 5, 7, 12, 16, 14}。
如果我们能在价格为5的时候买入并在价格为16时卖出，则能收获最大的利润11。
'''
'''主要思路：
首先明确一点：买入股票后才能卖出，因此直接用最大值减最小值是不行的，因为最大值可能出现在最小值前面。
如果把股票的买入价和卖出价两个数字组成数字对，那么利润就是这个数字对的差值（卖出-买入）。
因此，最大利润就是数组中所有数字对的最大差值：
思路1（时间O(n^2), 空间O(1)）：枚举。找出数组中所有的数对，求出它们的差值的最大值。
思路2（时间O(n), 空间O(1)）：显然，在卖出价固定时，买入价越低获得的利润越大。
也就是说，如果在遍历到数组中第i个数时，只要能够记录下之前的i-1个数字的最小值，
就能算出当前价位卖出时可能得到的最大利润
'''


class Solution:
    def MaxDiff1(self, numbers):
        if not numbers or len(numbers) < 2: return 0
        length = len(numbers)
        maxDiff = numbers[1] - numbers[0]
        for buy in range(length):
            for sell in range(buy + 1, length):  # 注意这里从buy+1开始
                curDiff = numbers[sell] - numbers[buy]
                if curDiff > maxDiff:
                    maxDiff = curDiff
        return max(maxDiff, 0)

    def MaxDiff2(self, numbers):
        if not numbers or len(numbers) < 2: return 0
        # 设置两个变量分别记录最小价格和最大利润
        maxProfit, minPrice = 0, float('inf')  # 设maxProfit为0可以保证出现负利润时返回0
        for price in numbers:
            minPrice = min(minPrice, price)  # 看一下目前有没有更低的价格来买入
            profit = price - minPrice  # 假如现在卖出能赚多少钱
            maxProfit = max(maxProfit, profit)  # 记录下最大利润，以便后面作参考比较
        return maxProfit


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[4, 1, 3, 2, 5], 4])
        testArgs.append([[1, 2, 4, 7, 11, 16], 15])  # 价格递增
        testArgs.append([[16, 11, 7, 4, 2, 1], 0])  # 价格递减，此时选择不买股票利润最高
        testArgs.append([[16, 16, 16, 16, 16], 0])  # 价格全部相同
        testArgs.append([[9, 11, 5, 7, 16, 1, 4, 2], 11])
        testArgs.append([[2, 4], 2])
        testArgs.append([[4, 2], 0])
        testArgs.append([[1], 0])
        testArgs.append([[], 0])
        testArgs.append([None, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

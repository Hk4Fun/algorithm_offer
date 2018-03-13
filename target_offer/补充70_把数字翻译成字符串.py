__author__ = 'Hk4Fun'
__date__ = '2018/3/5 12:22'

'''题目描述：
给定一个数字，按照如下规则翻译成字符串：0翻译成“a”，1翻译成“b”...25翻译成“z”。
一个数字有多种翻译可能，例如12258一共有5种，分别是bccfi，bwfi，bczi，mcfi，mzi。
实现一个函数，用来计算一个数字有多少种不同的翻译方法。
'''
'''主要思路：
动态规划（时间O(n),空间O(n)）。定义函数f(i)表示从第i位数字开始的不同翻译的数目，则状态转移方程为：
f(i) = f(i+1)+g(i,i+1)f(i+2)。当第i位和第i+1位两位数字拼接起来的数字在10~25的范围内时，
g(i,i+1)的值为1，否则为0。自底向上，在这里为从右向左翻译
'''


class Solution:
    def TranslationCount(self, number):
        if number == None or number < 0:
            return
        numberStr = str(number)
        length = len(numberStr)
        dp = [1] * length
        for i in range(length - 1, -1, -1):
            if i < length - 1:
                count = dp[i + 1]
            else:
                count = 1
            if i < length - 1 and 10 <= int(numberStr[i:i + 2]) <= 25:
                if i < length - 2:
                    count += dp[i + 2]
                else:
                    count += 1
            dp[i] = count
        return dp[0]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([0, 1])
        testArgs.append([10, 2])
        testArgs.append([125, 3])
        testArgs.append([126, 2])
        testArgs.append([426, 1])
        testArgs.append([100, 2])
        testArgs.append([101, 2])
        testArgs.append([12258, 5])
        testArgs.append([-100, None])
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

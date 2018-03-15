__author__ = 'Hk4Fun'
__date__ = '2018/3/15 16:01'
'''题目描述：
给定一个数，如何求它的平方根(不能使用内置函数，如sqrt()函数)。
'''
'''主要思路：
思路1（二分法）
思路2（牛顿迭代法）：
迭代公式：x_(n+1) = (x_n + num/x_n) / 2
推导过程采用切线逼近法，具体见：https://www.cnblogs.com/wangkundentisy/p/8118007.html

牛顿法同二分法一样，时间复杂度为O(logN)，空间复杂度为O(1)。
牛顿法每次迭代的误差都会至少小一半，迭代次数会小于二分法
'''


class Solution:
    def sqrt_binary(self, num, accuracy):
        if (not isinstance(num, float) and not isinstance(num, int)) or num < 0:
            return
        max = num
        min = 0
        mid = (min + max) / 2
        while abs(mid * mid - num) > accuracy:
            if mid * mid > num:
                max = mid
            elif mid * mid < num:
                min = mid
            else:
                return mid
            mid = (min + max) / 2
        return mid

    def sqrt_newton(self, num, accuracy):
        if (not isinstance(num, float) and not isinstance(num, int)) or num < 0:
            return
        x = 1  # 设置初值，初值的设置影响到计算的次数
        while abs(x * x - num) > accuracy:
            x = (x + num / x) / 2
        return x


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 100  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        import math

        testArgs.append([1, 1e-5, math.sqrt(1)])
        testArgs.append([2, 1e-5, math.sqrt(2)])
        testArgs.append([3, 1e-5, math.sqrt(3)])
        testArgs.append([4, 1e-5, math.sqrt(4)])
        testArgs.append([625, 1e-5, math.sqrt(625)])
        testArgs.append([1000, 1e-5, math.sqrt(1000)])
        testArgs.append([0, 1e-5, math.sqrt(0)])
        testArgs.append([-1, 1e-5, None])
        testArgs.append([-100, 1e-5, None])
        testArgs.append([1.1, 1e-5, math.sqrt(1.1)])
        testArgs.append([2.25, 1e-5, math.sqrt(2.25)])

        # 随机测试
        import random
        up_bound = 10000  # 随机数范围
        testNum = 1000  # 随机数个数
        accuracy = 1e-6  # 精度
        for i in range(testNum):
            num = random.random() * up_bound
            testArgs.append([num, accuracy, math.sqrt(num)])

        return testArgs

    def convert(self, result, *func_arg):
        return result

    def checked(self, result, expected, *func_arg):
        if result != None and expected != None and func_arg:
            sqrt_num = result
            num = func_arg[0]
            accuracy = func_arg[1]
            return abs(sqrt_num * sqrt_num - num) < accuracy
        if result == None and expected == None:
            return True


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

__author__ = 'Hk4Fun'
__date__ = '2018/4/5 14:20'
'''题目描述：
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 1, 2, 3, 4, 5, 6, 8, 9, 10, 12 is the sequence of the first 10 ugly numbers.
Note that 1 is typically treated as an ugly number, and n does not exceed 1690.
'''
'''主要思路：
target_offer34_丑数
时间O（n），空间O（n）
'''


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 7: return n
        idx2 = idx3 = idx5 = 0
        ugly = [1]
        for _ in range(1, n):
            u2, u3, u5 = ugly[idx2] * 2, ugly[idx3] * 3, ugly[idx5] * 5
            ugly.append(min(u2, u3, u5))
            if ugly[-1] == u2: idx2 += 1
            if ugly[-1] == u3: idx3 += 1
            if ugly[-1] == u5: idx5 += 1
        return ugly[-1]


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

        testArgs.append([1, 1])
        testArgs.append([2, 2])
        testArgs.append([3, 3])
        testArgs.append([4, 4])
        testArgs.append([5, 5])
        testArgs.append([6, 6])
        testArgs.append([7, 8])
        testArgs.append([8, 9])
        testArgs.append([9, 10])
        testArgs.append([10, 12])
        testArgs.append([11, 15])
        testArgs.append([1500, 859963392])
        testArgs.append([0, 0])

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
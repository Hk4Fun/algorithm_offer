__author__ = 'Hk4Fun'
__date__ = '2018/3/24 18:44'
'''题目描述：
Given a decimal number n and an integer k, Convert decimal number n to base-k.
注意事项:
1.0<=n<=2^31-1, 2<=k<=16
2.Each letter over 9 is indicated in uppercase
'''


class Solution:
    """
    @param n: a decimal number
    @param k: a Integer represent base-k
    @return: a base-k number
    """

    def hexConversion(self, n, k):
        if n == 0:
            return '0'
        res = ''
        while n:
            a = n % k
            if a <= 9:
                a = chr(ord('0') + a)
            else:
                a = chr(ord('A') + a - 10)
            res = a + res
            n //= k
        return res


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

        testArgs.append([123, 2, '1111011'])
        testArgs.append([123, 8, '173'])
        testArgs.append([123, 10, '123'])
        testArgs.append([30, 16, '1E'])

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

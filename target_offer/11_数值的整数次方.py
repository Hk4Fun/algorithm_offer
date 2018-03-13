__author__ = 'Hk4Fun'
__date__ = '2018/1/4 17:18'

'''题目描述：
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方
'''
'''主要思路：
注意点：
1、base = 0 且 exponent < 0 时发生除零错误；
2、exponent < 0 时要作倒数；
3、0^0=1
4、判断 base 是否等于 0 时不能直接 == ，
   因为base为浮点数，有误差。如果两个小数的差的绝对值很小，
   比如小于0.0000001，就可以认为它们相等；
5、乘方可以考虑用快速幂（递归实现）
'''


class Solution:
    def Power(self, base, exponent):
        # 位运算求绝对值，但位运算不支持浮点数，所以还是用内置的abs()
        # def my_abs(num):
        #     # n >> 31 取得n的符号，若n为正数，n >> 31 等于0，若n为负数，n >> 31 等于-1
        #     # 若n为正数，则 n^0 - 0=n，n不变
        #     # 若n为负数，则 n^-1 + 1 = n^0xffffffff + 1，相当于n连同符号位取反，再加1，
        #     # 由于n为负数，在内存中用补码表示，取反加一相当于补码的补码，变回原码，符号位又变回正
        #     # 所以 n^-1 + 1 相当于在有符号位数前面加负号，这里负数n就变成正数了
        #     return (num ^ (num >> 31)) - (num >> 31)

        def is_equal(num1, num2):
            return abs(num1 - num2) < 0.0000001

        def PowerWithUnsignedExponent(base, exponent):
            if exponent == 0:
                return 1
            if exponent == 1:
                return base
            result = PowerWithUnsignedExponent(base, exponent >> 1)  # 除2用位运算
            result *= result
            if exponent & 1 == 1:  # 判奇偶模2用位运算
                result *= base
            return result

        if is_equal(base, 0.0) and exponent < 0:
            return
        result = PowerWithUnsignedExponent(base, abs(exponent))
        if exponent < 0:
            return 1.0 / result
        return result


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        testArgs.append([2, 2, 4])  # 底数正数，指数正数
        testArgs.append([2, 0, 1])  # 底数正数，指数0
        testArgs.append([2, -2, 0.25])  # 底数正数，指数负数
        testArgs.append([0, 2, 0])  # 底数0，指数正数
        testArgs.append([0, 0, 1])  # 底数0，指数0
        testArgs.append([0, -2, None])  # 底数0，指数负数
        testArgs.append([-2, 2, 4])  # 底数负数，指数正数
        testArgs.append([-2, 0, 1])  # 底数负数，指数0
        testArgs.append([-2, -2, 0.25])  # 底数负数，指数负数
        testArgs.append([2, 33, 8589934592])  # 奇数次幂
        testArgs.append([2, 100, 1267650600228229401496703205376])  # 大数

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

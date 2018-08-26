__author__ = 'Hk4Fun'
__date__ = '2018/8/26 16:32'
'''题目描述：
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false
Follow up:
Could you do it without using any loop / recursion?
'''
'''主要思路：
https://leetcode.com/articles/power-of-three/

思路1：循环

思路2：进制转换
转换成3进制数，看最高位是否为1
这个思路和思路1没什么区别

思路3：取对数
如果是3次方数，那么以3为底取对数后应该是一个整数
但标准库中没有log3()，因此这里需要做一个转换：
log3(n) = log10(n)/log10(3)

思路4：整数上限
一个int也就最高到2147483647，那么3次方数不会超过3^19=1162261467
因此只需判断该数能否整除3^19即可
'''

from math import log10


class Solution:
    """
    :type n: int
    :rtype: bool
    """

    def isPowerOfThree1(self, n):
        if n < 1: return False
        while n % 3 == 0:
            n //= 3
        return n == 1

    def isPowerOfThree3(self, n):
        return (log10(n) / log10(3)) % 1 == 0 if n > 0 else False

    def isPowerOfThree4(self, n):
        return 1162261467 % n == 0 if n > 0 else False


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

        testArgs.append([0, False])
        testArgs.append([1, True])
        testArgs.append([3, True])
        testArgs.append([4, False])
        testArgs.append([6, False])
        testArgs.append([8, False])
        testArgs.append([9, True])
        testArgs.append([45, False])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

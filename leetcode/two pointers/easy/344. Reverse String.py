__author__ = 'Hk4Fun'
__date__ = '2018/4/11 19:43'
'''题目描述：
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''
'''主要思路：
时间O（n），空间O（1 or n）
本来不需要额外空间，但python字符串为不可变对象，所以只能先转成列表
'''


class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return ''
        l, r = 0, len(s) - 1
        s = list(s)  # python字符串为不可变对象，所以只能先转成列表
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)


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

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

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

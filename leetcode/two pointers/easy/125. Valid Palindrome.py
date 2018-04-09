__author__ = 'Hk4Fun'
__date__ = '2018/4/9 11:55'
'''题目描述：

'''
'''主要思路：
思路1：时间O（n），空间O（1）
首尾指针相向移动，遇到非数字字母跳过

思路1：时间O（n），空间O（n）
去掉非数字字母，然后翻转看是否一样
'''


class Solution:
    """
    :type s: str
    :rtype: bool
    """

    def isPalindrome_two_pointers(self, s):
        if s == '': return True
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum(): l += 1
            while l < r and not s[r].isalnum(): r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    def isPalindrome_reverse(self, s):
        s = [c for c in s.lower() if c.isalnum()]
        return s == s[::-1]


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

        testArgs.append(["A man, a plan, a canal: Panama", True])
        testArgs.append(["race a car", False])

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

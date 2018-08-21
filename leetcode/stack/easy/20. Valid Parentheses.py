__author__ = 'Hk4Fun'
__date__ = '2018/5/15 23:22'
'''题目描述：
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

Example 5:
Input: "{[]}"
Output: true
'''
'''主要思路：
时间O（n），空间O（n）
栈实现
'''


class Solution:
    """
    :type s: str
    :rtype: bool
    """

    def isValid1(self, s):
        stack = []
        for ch in s:
            if ch in '([{':
                stack.append(ch)
            else:  # ch in ')]}'
                if not stack:
                    return False
                top = stack.pop()
                if ch == ')' and top != '(':
                    return False
                elif ch == ']' and top != '[':
                    return False
                elif ch == '}' and top != '{':
                    return False
        return not stack

    def isValid2(self, s):  # 上一思路的精简版
        pair = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if stack and ch in pair:
                if stack[-1] != pair[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        return not stack

    def isValid3(self, s):  # pythonic
        while '()' in s or '{}' in s or '[]' in s:
            s = s.replace('{}', '').replace('()', '').replace('[]', '')
        return True if s == '' else False


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

        testArgs.append(['()', True])
        testArgs.append(['()[]{}', True])
        testArgs.append(['(]', False])
        testArgs.append(['([)]', False])
        testArgs.append(['{[]}', True])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

__author__ = 'Hk4Fun'
__date__ = '2018/5/10 15:19'
'''题目描述：
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
'''
'''主要思路：
target_offer/35_4_变位词.py
这里提供更加简洁的代码
时间O（n+m），空间O（1）
'''

from collections import Counter


class Solution:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    def isAnagram1(self, s, t):
        if len(s) != len(t): return False
        table = [0] * 256
        for i, j in zip(map(ord, s), map(ord, t)):
            table[i] += 1
            table[j] -= 1
        return table == [0] * 256

    def isAnagram2(self, s, t):
        return Counter(s) == Counter(t)


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
    MyTest(Solution()).start_test()

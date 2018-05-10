__author__ = 'Hk4Fun'
__date__ = '2018/5/10 16:44'
'''题目描述：
Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
'''
'''主要思路：
target_offer/35_1_第一个只出现一次的字符.py 思路1（思路2 TLE了）
时间O（n），空间O（1）
'''


class Solution:
    """
    :type s: str
    :rtype: int
    """
    def firstUniqChar1(self, s):
        table = [0] * 26
        for i in s:
            table[ord(i) - ord('a')] += 1
        for i, v in enumerate(s):
            if table[ord(v) - ord('a')] == 1: return i
        return -1

    def firstUniqChar2(self, s): # TLE了
        res = [i for i in range(len(s)) if s.count(s[i]) == 1]
        return res[0] if res else -1

    def firstUniqChar3(self, s): # 这个没有TLE，对比思路2，虽然都用s.count，但思路2的for范围是整个字符串s
        index = [s.index(l) for l in 'abcdefghijklmnopqrstuvwxyz' if s.count(l) ==1]
        return min(index) if index else -1

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
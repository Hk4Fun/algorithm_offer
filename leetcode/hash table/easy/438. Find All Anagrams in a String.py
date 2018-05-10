__author__ = 'Hk4Fun'
__date__ = '2018/5/10 22:17'
'''题目描述：
Given a string s and a non-empty string p, 
find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only 
and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''
'''主要思路：
时间O（n），空间O（1）, n为s的长度
不必统计每个子串，这样会TLE，采用滑动窗口
'''

from collections import defaultdict


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s) < len(p): return []
        res = []
        table_s, table_p = defaultdict(int), defaultdict(int)
        for i in range(len(p)):
            table_s[s[i]] += 1
            table_p[p[i]] += 1
        for i in range(len(s) - len(p)):
            if table_s == table_p: res.append(i)
            # 窗口右边界右移
            if s[i + len(p)] not in table_s:
                table_s[s[i + len(p)]] = 1
            else:
                table_s[s[i + len(p)]] += 1
            table_s[s[i]] -= 1  # 窗口左边界右移
            if table_s[s[i]] == 0:  # 减到0就从表中删除
                del table_s[s[i]]
        if table_s == table_p: res.append(len(s) - len(p))  # 最后一个窗口（子串）
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

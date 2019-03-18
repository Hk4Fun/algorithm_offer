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
注意到易位词只关心字母出现的频次是否相等而不关心字母排列顺序是否相等
所以可以使用字典（哈希表）统计字母出现的频次：
使用table_p统计p的字母频次，然后使用table_s统计s，
窗口长度为p的长度，随着窗口不断右移，table_s不断被更新，
每次比较table_p是否等于table_s，是则说明出现易位词
'''


class Solution:
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """

    def findAnagrams1(self, s, p): # 暴力解法，直接 TLE 了
        def isAnagram(s1, s2):
            d = [0] * 26
            for ch in s1:
                d[ord(ch) - ord('a')] += 1
            for ch in s2:
                d[ord(ch) - ord('a')] -= 1
            return d == [0] * 26

        res = []
        for i in range(0, len(s) - len(p) + 1):
            if isAnagram(s[i:i + len(p)], p):
                res.append(i)
        return res

    def findAnagrams2(self, s, p):
        if len(s) < len(p): return []
        table_s, table_p, res = {}, {}, []
        for i in range(len(p)):
            table_s[s[i]] = table_s.setdefault(s[i], 0) + 1
            table_p[p[i]] = table_p.setdefault(p[i], 0) + 1
        for i in range(len(s) - len(p)):
            if table_s == table_p: res.append(i)
            table_s[s[i + len(p)]] = table_s.setdefault(s[i + len(p)], 0) + 1  # 窗口右边界右移
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

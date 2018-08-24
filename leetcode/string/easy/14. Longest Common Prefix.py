__author__ = 'Hk4Fun'
__date__ = '2018/8/24 17:12'
'''题目描述：
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
'''主要思路：
思路1：时间O（n∗minLen），空间O（1） n表示字符串个数，minLen表示最短的字符串长度
以最短的字符串为标杆，‘垂直扫描’其他的字符串
不匹配时结束扫描，都匹配则说明LCP正好是那个最短的字符串

思路2：pythonic
仍然是‘垂直扫描’，但使用zip()把垂直的字符放在同一个set中去重，
如果set中只有一个字符说明匹配前缀

思路3：trie，时间O（S），空间O（S），S表示所有字符串的长度总和
先建立一棵前缀树，从根节点往下直到第一个分叉点，一路上所经过的字符串就是最长前缀
'''


class Solution:
    """
    :type strs: List[str]
    :rtype: str
    """

    def longestCommonPrefix1(self, strs):
        if not strs: return ''
        if len(strs) == 1: return strs[0]
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

    def longestCommonPrefix2(self, strs):
        if not strs: return ""
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        else:
            return min(strs)  # LCP正好是最短的那个字符串

    def longestCommonPrefix3(self, strs):
        def buidTrie(strs):  # 根据strs构建一棵trie
            root = {}
            for s in strs:
                curdict = root
                for ch in s:
                    curdict = curdict.setdefault(ch, {})
                curdict['/'] = '/'  # 结束符，表示已经到达字符串末尾
            return root

        curdict = buidTrie(strs)
        lcp = ''
        while len(curdict) == 1 and curdict != '/':
            ch, curdict = curdict.popitem()
            lcp += ch if ch != '/' else ''
        return lcp


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

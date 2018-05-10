__author__ = 'Hk4Fun'
__date__ = '2018/5/10 17:53'
'''题目描述：
Given a string which consists of lowercase or uppercase letters, 
find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.
Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
'''
'''主要思路：
时间O（n），空间O（1）:
先使用Counter统计出各字母次现的次数，为了构造最长回文串，采用贪婪算法：
如果这个字母出现了偶数次，那么可以全部加入回文串中（对称放两边）；
如果这个字母出现了奇数次，那么先拿出一个把剩下的偶数个加入回文串中（对称放两边）；
然后看拿出的那个能否放进回文串中：
如果此时回文串的长度为偶数，说明没有中心，可以把刚刚拿出来的那个字母放到回文串的中间；
如果此时回文串的长度为奇数，说明已经存在中心，丢弃刚刚拿出来的那个字母
'''

from collections import Counter


class Solution:
    """
    :type s: str
    :rtype: int
    """

    def longestPalindrome(self, s):
        res = 0
        for v in Counter(s).values():
            res += v // 2 * 2  # 相当于拿出偶数个字符放两边
            if res % 2 == 0 and v % 2 == 1: res += 1  # 相当于添加中心
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

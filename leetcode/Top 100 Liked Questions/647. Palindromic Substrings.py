__author__ = 'Hk4Fun'
__date__ = '2018/7/23 23:24'
'''题目描述：
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes 
are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''
'''主要思路：
思路1：时间O（n^2），空间O（1）
利用回文串(l, r)的(l+1, r-1)子串也是回文串，可以遍历2*n-1个中心，
向外扩展，直到不能成为回文串为止

思路2：时间O（n），空间O（n）
leetcode/dp/medium/5. Longest Palindromic Substring.py
manacher算法求出每个中心的最长回文子串半径（线性时间），然后遍历该数组，
累计(i+1)//2，因为回文串(l, r)的(l+1, r-1)子串也是回文串
'''


class Solution:
    """
    :type s: str
    :rtype: int
    """

    def countSubstrings1(self, s):
        count = 0
        for i in range(2 * len(s) - 1):
            l, r = i // 2, (i // 2) + (i % 2)
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                count += 1
        return count

    def countSubstrings2(self, s):
        def manacher(s):
            s = '$#{}#%'.format('#'.join(s))
            arr = [0] * len(s)
            center = right = 0
            for i in range(1, len(s) - 1):
                arr[i] = i < right and min(arr[2 * center - i], right - i)
                while s[i + arr[i] + 1] == s[i - arr[i] - 1]: arr[i] += 1
                if i + arr[i] > right: center, right = i, i + arr[i]
            return arr

        return sum((i + 1) // 2 for i in manacher(s))


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

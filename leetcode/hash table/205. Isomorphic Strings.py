__author__ = 'Hk4Fun'
__date__ = '2018/5/10 14:05'
'''题目描述：
Given two strings s and t, determine if they are isomorphic.

Two strings are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
Note:
You may assume both s and t have the same length.
'''
'''主要思路：
思路1：时间O（n），空间O（1）
两张哈希表分别记录两个字符串中字符上次出现的位置，由于都是字母，所以最多256
如果两个字符串相同位置的字符在上次出现的位置不一样则说明不同构。
注意在记录位置时是i+1而不是i，因为初始化的时候为0，
如果是i的话就区分不开上一次出现的位置在0号位和没出现过该字符的情况，
因为没出现过的字符的值都是0。
举个例子，如果每次赋值i而不是i+1，那么字符串"aa"和字符串"cd"就会出现误判，
在第二次循环是由于m1['a']=0，而m2['d']=0，所以程序最后返回的是true，但是显然应该返回false。

思路2：
pythonic, 一行解决。（beat 100%）
如果set(zip(s, t))，set(s), set(t)三者的长度一样，则为同构

思路3：
pythonic, 一行解决。
用find找到字符在字符串中首次出现的位置，都一样则为同构
注意与思路1的区别，思路1是记录字符在字符串中最近一次（上一次）出现的位置
'''


class Solution:
    """
    :type s: str
    :type t: str
    :rtype: bool
    """

    def isIsomorphic1(self, s, t):
        s_table, t_table = [0] * 256, [0] * 256
        for i in range(len(s)):
            s_char, t_char = ord(s[i]), ord(t[i])
            if s_table[s_char] != t_table[t_char]: return False
            s_table[s_char] = t_table[t_char] = i + 1
        return True

    def isIsomorphic2(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

    def isIsomorphic3(self, s, t):
        return map(s.find, s) == map(t.find, t)

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

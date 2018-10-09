__author__ = 'Hk4Fun'
__date__ = '2018/2/11 0:48'

'''题目描述：
在一个字符串(1<=字符串长度<=10000，全部由字母组成)中找到第一个只出现一次的字符,并返回它的位置,不存在就返回-1
'''
'''主要思路：
思路1：利用python的字典建立哈希表，键记录字母，值记录字母出现的次数。
       第一次遍历建立哈希表，第二次遍历找到第一个值为1的键（字母）。
       时间复杂度O(n)，空间复杂度O(1)（不会超过256个键值对）
思路2：pythonic，利用count()
'''

from collections import OrderedDict


class Solution:
    def FirstNotRepeatingChar1(self, s):
        hashTable = OrderedDict()
        for ch in s:
            hashTable[ch] = hashTable.setdefault(ch, 0) + 1
        for ch, v in hashTable.items():
            if v == 1:
                return s.index(ch)
        return -1

    def FirstNotRepeatingChar2(self, s):
        if not s:
            return -1
        result = [i for i in range(len(s)) if s.count(s[i]) == 1]
        if result:
            return result[0]
        return -1


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 存在只出现一次的字符
        testArgs.append(['google', 4])

        # 不存在只出现一次的字符
        testArgs.append(['aabccdbd', -1])

        # 所有字符都只出现一次
        testArgs.append(['abcdefg', 0])

        # 长串，包含大小写
        testArgs.append(['NXWtnzyoHoBhUJaPauJaAitLWNMlkKwDYbbigdMMaYfkVPhGZcrEwp', 1])

        # 空串
        testArgs.append(['', -1])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

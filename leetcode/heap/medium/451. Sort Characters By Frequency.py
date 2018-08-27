__author__ = 'Hk4Fun'
__date__ = '2018/8/27 20:57'
'''题目描述：
Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input:
"cccaaa"

Output:
"cccaaa"

Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
'''
'''主要思路：
思路1：时间O（nlogn），空间O（n）
hashmap + sort
先统计词频，然后根据词频排序key

思路2：时间O（n），空间O（n）
先统计词频，然后多开一个长度为len(s)的数组，其构造为[[ch,],]
因为某个字符的出现次数不可能超过s的长度，
所以我们将每个字符根据其出现次数放入数组中的对应位置，
那么最后我们只要从后往前遍历数组所有位置，
将不为空的位置的字符串加入结果res中即可
'''

from collections import Counter


class Solution:
    """
    :type s: str
    :rtype: str
    """

    def frequencySort1(self, s):
        return ''.join(ch * n for ch, n in Counter(s).most_common())

    def frequencySort2(self, s):
        t = [[] for _ in range(len(s) + 1)]
        for ch, n in Counter(s).items():
            t[n].append(ch)
        return ''.join(ch * i for i in range(len(s), -1, -1) for ch in t[i])


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

        # testArgs.append(['tree', 'eert'])
        testArgs.append(['eeeee', 'eeeee'])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

__author__ = 'Hk4Fun'
__date__ = '2018/3/25 17:26'
'''题目描述：
实现一个算法确定字符串中的字符是否均唯一出现
样例
给出"abc"，返回 true
给出"aab"，返回 false
'''
'''主要思路：
思路1（时间O（n），空间O（1））：
假设字符集是ASCII字符，那么我们可以开一个大小为256的bool数组来表征每个字符的出现。
数组初始化为false，遍历一遍字符串中的字符，当bool数组对应位置的值为真， 
表明该字符在之前已经出现过，即可得出该字符串中有重复字符。否则将该位置的bool数组 值置为true

思路2（时间O（n），空间O（1））：
我们还可以通过位运算来减少空间的使用量。 用每一位表征相应位置字符的出现。
对于ASCII字符，我们需要256位，即一个长度为8的int 数组a即可。
这里的关键是要把字符对应的数字，映射到正确的位上去。比如字符’b’对应的代码是98，
那么我们应该将数组中的哪一位置为1呢？
用98除以32，得到对应数组a的下标：3。98对32取模得到相应的位：2。相当于计算行和列

思路3（时间O（n），空间O（n））：pythonic，使用集合set来去重
'''


class Solution:
    """
    @param: str: A string
    @return: a boolean
    """

    def isUnique1(self, str):
        a = [False] * 256
        for s in str:
            i = ord(s)
            if a[i]: return False
            a[i] = True
        return True

    def isUnique2(self, str):
        a = [0] * 8
        for s in str:
            i = ord(s)
            index, shift = i // 32, i % 32
            if (a[index] & (1 << shift)): return False
            a[index] |= (1 << shift)
        return True

    def isUnique3(self, str):
        return len(set(str)) == len(str)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append(['aabc', False])
        testArgs.append(['abCc', True])

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

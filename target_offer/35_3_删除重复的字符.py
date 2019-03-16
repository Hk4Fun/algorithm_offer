__author__ = 'Hk4Fun'
__date__ = '2018/2/11 14:29'

'''题目描述：
定义一个函数，删除字符串中所有重复出现的字符，使重复的字符只出现一次，且保持字符顺序不变
例如输入"google"，删除重复字符后的结果为"gole"
'''
'''主要思路：
思路1：pythonic，把 OrderedDict 当作 OrderedSet 来使用
思路2：自己用字典来保存出现过的字符，注意，py3.6之后的字典都是有序字典了
'''

from collections import OrderedDict


class Solution:
    def del_dup1(self, s):
        if s is None: return
        return ''.join(OrderedDict.fromkeys(s).keys())

    def del_dup2(self, s):
        if s is None: return
        res = {}
        for ch in s:
            res[ch] = 1
        return ''.join(res.keys())


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 有重复字符
        testArgs.append(['google', 'gole'])

        # 没有重复字符
        testArgs.append(['gole', 'gole'])

        # 全是重复字符
        testArgs.append(['aasssdddd', 'asd'])

        # 空串
        testArgs.append(['', ''])

        # None
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

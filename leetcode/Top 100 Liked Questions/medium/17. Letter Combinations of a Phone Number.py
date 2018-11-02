__author__ = 'Hk4Fun'
__date__ = '2018/8/12 16:57'
'''题目描述：
Given a string containing digits from 2-9 inclusive, 
return all possible letter combinations that the number could represent.
A mapsping of digit to letters (just like on the telephone buttons) is given below. 
{'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
Note that 1 does not maps to any letters.
'''
'''主要思路：
回溯法
'''

from functools import reduce


class Solution:
    """
    :type digits: str
    :rtype: List[str]
    """

    def letterCombinations1(self, digits):
        if not digits: return []
        maps = {'2': 'abc',
                '3': 'def',
                '4': 'ghi',
                '5': 'jkl',
                '6': 'mno',
                '7': 'pqrs',
                '8': 'tuv',
                '9': 'wxyz'}

        def bt(idx):
            if idx == len(digits) - 1:
                return list(maps[digits[idx]])
            res = []
            for ch in maps[digits[idx]]:
                for s in bt(idx + 1):
                    res.append(ch + s)
            return res

        return bt(0)

    def letterCombinations2(self, digits):  # 简化版，使用reduce
        if not digits: return []
        maps = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        return reduce(lambda acc, digit: [x + y for x in acc for y in maps[digit]], digits, [''])


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

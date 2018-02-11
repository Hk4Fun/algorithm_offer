__author__ = 'Hk4Fun'
__date__ = '2018/2/11 14:29'

'''题目描述：
定义一个函数，删除字符串中所有重复出现的字符，使重复的字符只出现一次，且保持字符顺序不变
例如输入"google"，删除重复字符后的结果为"gole"
'''
'''主要思路：
遍历字符串，用用列表或字典保存前面没出现过的字符
'''


class Solution:
    def del_dup1(self, s):  # 列表保存
        if s == None:
            return
        result = []
        for i in s:
            if i not in result:
                result.append(i)
        return ''.join(result)

    def del_dup2(self, s):  # 用字典保存，可索引字符
        if s == None:
            return
        result = {}
        for i in s:
            try:
                if result[i]:
                    continue
            except KeyError:
                result[i] = True
        return ''.join(result.keys())


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

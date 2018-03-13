__author__ = 'Hk4Fun'
__date__ = '2018/2/11 13:50'

'''题目描述：
定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符。
例如从第一个字符串"We are students."中删除在第二个字符串"aeiou"中出现过的字符
得到的结果是"W r stdnts."
'''
'''主要思路：
思路1：遍历s1，检查s1的每个字符是否在s2中出现
思路2：将s2建立一张哈希表，这样在检查s1的每个字符是否在s2中出现时可以O(1)
'''


class Solution:
    def delete_char1(self, s1, s2):
        if s1 == None or s2 == None:
            return
        return ''.join([i for i in s1 if i not in s2])

    def delete_char2(self, s1, s2):
        if s1 == None or s2 == None:
            return
        d = dict(zip(s2, [1] * len(s2)))
        result = []
        for i in s1:
            try:
                if d[i]:
                    continue
            except KeyError:
                result.append(i)
        return ''.join(result)

    def delete_char3(self, s1, s2):
        if s1 == None or s2 == None:
            return
        d = dict(zip(s2, [1] * len(s2)))
        result = []
        for i in s1:
            if i not in d.keys():
                result.append(i)
        return ''.join(result)
# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # s1中有s2字符
        testArgs.append(['We are students.', 'aeiou', 'W r stdnts.'])

        # s1中没有s2字符
        testArgs.append(['We are students.', 'xkyz', 'We are students.'])

        # s1和s2相等
        testArgs.append(['We are students.', 'We are students.', ''])

        # s1的字符种数小于s2
        testArgs.append(['We are students.', 'We are students.xkyz', ''])

        # s1为空串
        testArgs.append(['', 'aeiou', ''])

        # s2为空串
        testArgs.append(['We are students.', '', 'We are students.'])

        # s1和s2都为空串
        testArgs.append(['', '', ''])

        # s1和s2都为None
        testArgs.append([None, None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

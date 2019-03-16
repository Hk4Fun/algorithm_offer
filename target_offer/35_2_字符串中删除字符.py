__author__ = 'Hk4Fun'
__date__ = '2018/2/11 13:50'

'''题目描述：
定义一个函数，输入两个字符串，从第一个字符串中删除在第二个字符串中出现过的所有字符。
例如从第一个字符串"We are students."中删除在第二个字符串"aeiou"中出现过的字符
得到的结果是"W r stdnts."
'''
'''主要思路：
思路1(时间O(n*m), 空间O(1)) ：遍历 s1，检查 s1 的每个字符是否在 s2 中出现
思路2(时间O(n), 空间O(m)) ：将 s2 转换成一个集合，这样在检查 s1 的每个字符是否在 s2 中出现时可以 O(1)
'''


class Solution:
    def delete_char1(self, s1, s2):
        if s1 is None or s2 is None: return
        return ''.join(ch for ch in s1 if ch not in s2)

    def delete_char2(self, s1, s2):
        if s1 is None or s2 is None: return
        s = set(s2)
        return ''.join(ch for ch in s1 if ch not in s)


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

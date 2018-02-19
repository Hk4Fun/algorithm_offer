__author__ = 'Hk4Fun'
__date__ = '2018/2/19 1:07'

'''题目描述：
将一个字符串转换成一个整数，要求不能使用字符串转换整数的库函数。 数值为0或者字符串不是一个合法的数值则返回0
'''
'''主要思路：
考虑这么几点：
1、有无正负号
2、只有正负号
3、多个正负号开头
4、空串或None
5、非法字符
由于python整型无限长，所以不考虑正负溢出
（一般对于32位整型来讲，最大正整数是0x7fffffff，最小负整数是0x80000000）
'''


class Solution:
    def StrToInt1(self, s):
        if not s:
            return 0
        start = 0  # 标记开始转换的位置
        minus = False  # 标记正负
        if s[0] == '-':
            start = 1
            minus = True
        elif s[0] == '+':
            start = 1
        sum = 0
        for i in range(start, len(s)):
            if s[i] < '0' or s[i] > '9':  # 含有非法字符返回0
                return 0
            sum = sum * 10 + ord(s[i]) - ord('0')
        return -1 * sum if minus else sum

    def StrToInt2(self, s):  # 使用内置转换函数来对比性能
        try:
            return int(s)
        except Exception:
            return 0


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append(['123', 123])
        testArgs.append(['+123', 123])
        testArgs.append(['-123', -123])
        testArgs.append(['1a33', 0])
        testArgs.append(['+0', 0])
        testArgs.append(['-0', 0])
        testArgs.append(['0', 0])
        testArgs.append(['+', 0])
        testArgs.append(['-', 0])
        testArgs.append(['++123', 0])
        testArgs.append(['--123', 0])
        testArgs.append(['+1-23', 0])
        testArgs.append(['0000', 0])
        testArgs.append(['', 0])
        testArgs.append([None, 0])
        testArgs.append(['+999999999999999999', 999999999999999999])
        testArgs.append(['-999999999999999999', -999999999999999999])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

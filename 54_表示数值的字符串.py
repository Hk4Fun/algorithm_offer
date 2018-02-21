__author__ = 'Hk4Fun'
__date__ = '2018/2/21 1:31'

'''题目描述：
请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。
例如，字符串"+100","5e2","-123","3.1416"和"-1E-16"都表示数值。
但是"12e","1a3.14","1.2.3","+-5"和"12e+4.3"都不是。
'''
'''主要思路：
数字的格式可以用A[.[B]][e|EC]或者.B[e|EC]表示，其中A和C都是整数（可以有正负号，也可以没有），
而B是一个无符号整数。考虑这么几种情况：
对于小数点'.'，前后A和B的出现形成或的关系：
1. 小数可以没有整数部分，例如.123等于0.123；
2. 小数点后面可以没有数字，例如233.等于233.0；
3. 当然小数点前面和后面可以有数字，例如233.666
4. 但不能单独出现小数点'.'
对于指数符号e或E，前后形成与的关系：
当e或E前面没有数字时，整个字符串不能表示数字，例如.e1、e1；
当e或E后面没有整数时，整个字符串不能表示数字，例如12e、12e+5.4

思路1：使用float()转换，利用是否抛出异常进行判断
思路2：正则表达式re匹配
思路3：从头到尾遍历字符串，按照逻辑一个个判断
'''


class Solution:
    def isNumeric1(self, s):
        try:
            float(s)
            return True
        except Exception:
            return False

    def isNumeric2(self, s):
        import re
        if s:
            return True if re.match(r'^[+-]?(\d+|(\.\d+)|(\d+\.)|(\d+\.\d+))([eE][+-]?\d+)?$', s) else False
        return False

    def isNumeric3(self, s):
        def scanUnsignedInteger(s):
            beforeLength = len(s)
            while s and s[0] >= '0' and s[0] <= '9':
                s.pop(0)
            return len(s) < beforeLength

        def scanInteger(s):
            if s and (s[0] == '+' or s[0] == '-'):
                s.pop(0)
            return scanUnsignedInteger(s)

        if not s:
            return False
        s = list(s)
        numeric = scanInteger(s)
        if s and s[0] == '.':
            s.pop(0)
            numeric = scanUnsignedInteger(s) or numeric

        if s and (s[0] == 'e' or s[0] == 'E'):
            s.pop(0)
            numeric = scanInteger(s) and numeric
        return numeric and s == []


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append(["100", True])
        testArgs.append(["123.45e+6", True])
        testArgs.append(["+500", True])
        testArgs.append(["5e2", True])
        testArgs.append(["3.1416", True])
        testArgs.append(["600.", True])
        testArgs.append(["-.123", True])
        testArgs.append(["-1E-16", True])
        testArgs.append(["1.79769313486232E+308", True])
        testArgs.append(['1.', True])
        testArgs.append(['.1', True])
        testArgs.append(['-.1e123', True])
        testArgs.append(['+1.E0', True])

        testArgs.append(["12e", False])
        testArgs.append(["1a3.14", False])
        testArgs.append(["1+23", False])
        testArgs.append(["1.2.3", False])
        testArgs.append(["+-5", False])
        testArgs.append(["12e+5.4", False])
        testArgs.append([".", False])
        testArgs.append(["+", False])
        testArgs.append(["+.", False])
        testArgs.append([".e1", False])
        testArgs.append(["e1", False])
        testArgs.append(["-.1e.", False])
        testArgs.append(["-.1e-1.", False])
        testArgs.append(['', False])
        testArgs.append([None, False])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

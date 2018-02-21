__author__ = 'Hk4Fun'
__date__ = '2018/2/20 23:08'

'''题目描述：
请实现一个函数用来匹配包括'.'和'*'的正则表达式。
模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（包含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。
例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但是与"aa.a"和"ab*a"均不匹配
'''
'''主要思路：
当模式中的第二个字符是“*”时：
如果字符串第一个字符跟模式第一个字符不匹配，则模式后移2个字符，字符串不变，继续匹配；
如果字符串第一个字符跟模式第一个字符匹配，可以有3种匹配方式：
1、字符串后移1字符，模式不变，即继续匹配字符下一位，因为*可以匹配多位；
2、模式后移2字符，字符串不变，相当于x*被忽略；
3、字符串后移1字符，模式后移2字符；
其中第三种情况可以由前两种组合，所以可以省略

而当模式中的第二个字符不是“*”时：
1、如果字符串第一个字符和模式中的第一个字符相匹配，那么字符串和模式都后移一个字符，接着匹配剩余的。
2、如果字符串第一个字符和模式中的第一个字符相不匹配，直接返回false。
'''


class Solution:
    def match1(self, s, pattern):
        if s == None or pattern == None:
            return False
        if s == '' and pattern == '':
            return True
        if s != '' and pattern == '':
            return False
        if len(pattern) > 1 and pattern[1] == '*':
            if s != '' and (pattern[0] == s[0] or pattern[0] == '.'):
                return self.match1(s[1:], pattern) \
                       or self.match1(s, pattern[2:]) \
                    # or self.match(s[1:], pattern[2:]) # 该情况可以由前两种情况组合，所以可以省略
            else:
                return self.match1(s, pattern[2:])
        if s != '' and (s[0] == pattern[0] or pattern[0] == '.'):
            return self.match1(s[1:], pattern[1:])
        return False

    def match2(self, s, pattern):  # 用re标准库进行性能对比
        import re
        if s == None or pattern == None:
            return False
        return True if re.match(pattern + '$', s) else False


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append(["", "", True])
        testArgs.append(["", ".*", True])
        testArgs.append(["", ".", False])
        testArgs.append(["", "c*", True])
        testArgs.append(["a", ".*", True])
        testArgs.append(["a", "a.", False])
        testArgs.append(["a", "", False])
        testArgs.append(["a", ".", True])
        testArgs.append(["a", "ab*", True])
        testArgs.append(["a", "ab*a", False])
        testArgs.append(["aa", "aa", True])
        testArgs.append(["aa", "a*", True])
        testArgs.append(["aa", ".*", True])
        testArgs.append(["aa", ".", False])
        testArgs.append(["ab", ".*", True])
        testArgs.append(["ab", ".", False])
        testArgs.append(["aaa", "aa*", True])
        testArgs.append(["aaa", "aa.a", False])
        testArgs.append(["aaa", "a.a", True])
        testArgs.append(["aaa", ".a", False])
        testArgs.append(["aaa", "a*a", True])
        testArgs.append(["aaa", "ab*a", False])
        testArgs.append(["aaa", "ab*ac*a", True])
        testArgs.append(["aaa", "ab*a*c*a", True])
        testArgs.append(["aaa", ".*", True])
        testArgs.append(["aab", "c*a*b", True])
        testArgs.append(["aaca", "ab*a*c*a", True])
        testArgs.append(["aaba", "ab*a*c*a", False])
        testArgs.append(["bbbba", ".*a*a", True])
        testArgs.append(["bcbbabab", ".*a*a", False])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

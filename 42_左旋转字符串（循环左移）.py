__author__ = 'Hk4Fun'
__date__ = '2018/2/15 19:43'

'''题目描述：
汇编语言中有一种移位指令叫做循环左移（ROL），现在有个简单的任务，就是用字符串模拟这个指令的运算结果。
对于一个给定的字符序列S，请你把其循环左移K位后的序列输出。
例如，字符序列S=”abcXYZdef”,要求输出循环左移3位后的结果，即“XYZdefabc”。
'''
'''主要思路：
思路1：先分片后拼接
思路2：先拼接后分片
思路3：原理：YX = (X^T*Y^T)^T
       相当于“翻转单词顺序”的特例，即翻转s[:n]和s[n:]这两部分，
       所以可以借鉴“翻转单词顺序”的思路，先翻转字符串的前面n个字符，
       再翻转字符串的后面部分，最后翻转整个字符串
       （这里若要先翻转整个字符串，则后面应翻转字符串的前面（len(s)-n）个字符再翻转字符串的后面部分）
       
'''


class Solution:
    def LeftRotateString1(self, s, n):
        if not s or n < 0:
            return ''
        n = n % len(s)  # 考虑重复左移，所以n % len(s)
        return s[n:] + s[:n]

    def LeftRotateString2(self, s, n):
        if not s or n < 0:
            return ''
        length = len(s)
        n = n % length
        return (s + s)[n:n + length]

    def LeftRotateString3(self, s, n):
        def reverse(s, start, end):
            if not s:
                return ''
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            return ''.join(s)

        if not s or n < 0:
            return ''
        length = len(s)
        n = n % length
        s = list(s)
        reverse(s, 0, n - 1)  # 先翻转字符串的前面n个字符
        reverse(s, n, length - 1)  # 再翻转字符串的后面部分
        reverse(s, 0, length - 1)  # 最后翻转整个字符串
        return ''.join(s)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append(['abcdefg', -1, ''])

        testArgs.append(['abcdefg', 0, 'abcdefg'])

        testArgs.append(['abcdefg', 1, 'bcdefga'])

        testArgs.append(['abcdefg', 2, 'cdefgab'])

        testArgs.append(['abcdefg', 6, 'gabcdef'])

        testArgs.append(['abcdefg', 7, 'abcdefg'])

        testArgs.append(['abcdefg', 8, 'bcdefga'])

        testArgs.append(['abcdefg', 23, 'cdefgab'])

        testArgs.append(['', 6, ''])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

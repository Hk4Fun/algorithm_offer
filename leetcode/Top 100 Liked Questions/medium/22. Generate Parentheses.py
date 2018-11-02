__author__ = 'Hk4Fun'
__date__ = '2018/7/29 10:01'
'''题目描述：
Given n pairs of parentheses, 
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
'''
'''主要思路：
思路1：时间O（2^(2n)），空间O（2^(2n)）
回溯法，暴力枚举所有情况，然后检查是否有效

思路2：时间O（4^n/sqr(n)），空间O（4^n/sqr(n)）
一边生成一边剪枝，使得最后生成的字符串（长度为2n）一定是有效的
用l记录左括号数，r记录右括号数，
只有当 l < n 时，左括号才能继续添加；
只有当 r < l 时，右括号数才能继续添加 
'''


class Solution:
    """
    :type n: int
    :rtype: List[str]
    """

    def generateParenthesis1(self, n):
        def generate(s=[]):
            if len(s) == 2 * n:
                if valid(s):
                    res.append(''.join(s))
            else:
                s.append('(')
                generate(s)
                s.pop()
                s.append(')')
                generate(s)
                s.pop()

        def valid(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                else:
                    count -= 1
                if count < 0: return False
            return count == 0

        res = []
        generate()
        return res

    def generateParenthesis2(self, n):
        def generate(s='', r=0, l=0):
            if len(s) == 2 * n:
                res.append(s)
                return
            if l < n: generate(s + '(', r, l + 1)
            if r < l: generate(s + ')', r + 1, l)

        res = []
        generate()
        return res

    def generateParenthesis2_simplify(self, n):
        def generate(s='', l=n, r=n, res=[]):
            # 如果是 res = res + s 就会报错，因为res为list而s为str
            # 但这里是res += s，为原地修改，因此相当于res.append(s)
            # 如果s是不可迭代的，如int，那么必须加上逗号转成tuple：res += s,
            # += 比 append() 快
            if not r: res += s  # 没有剩下的右括号可以添加了，说明整个字符串生成
            if l:     generate(s + '(', l - 1, r)  # 注意这里是 l - 1
            if r > l: generate(s + ')', l, r - 1)  # 注意这里是 r > l，r - 1
            return res

        return generate()


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

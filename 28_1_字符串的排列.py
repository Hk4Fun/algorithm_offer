__author__ = 'Hk4Fun'
__date__ = '2018/2/5 21:57'

'''题目描述：
输入一个字符串,按字典序打印出该字符串中字符的所有排列。
例如输入字符串abc,则打印出由字符a,b,c所能排列出来的所有字符串abc,acb,bac,bca,cab和cba。
输入描述:
输入一个字符串,长度不超过9(可能有字符重复),字符只包括大小写字母。
'''
'''主要思路：
思路1：经典方法，基于回溯法，图解：http://ox186n2j0.bkt.clouddn.com/Permutation%20of%20String.png
       递归，每次固定第一个字符，排列后面的字符，再拿第一个字符和它后面的字符逐个交换
思路2：递归，但不再固定第一个字符，而是从头到尾逐个字符抽出来，剩下字符的进行排列，所以也不用交换
       最后再把抽出来的那个字符与排列好的字符串拼在一起返回即可，只剩下一个字符时直接返回该字符
思路3：pythonic，使用itertools.permutations()
'''
import itertools


class Solution:
    def Permutation1(self, ss):
        def permutation(string, begin):
            if begin == len(string) - 1:
                result.append(''.join(string))  # 来到字符串末尾，结束一次排列
            else:
                for i in range(begin, len(string)):
                    string[begin], string[i] = string[i], string[begin]  # 把第一个字符和它后面的字符逐个交换
                    permutation(string, begin + 1)  # 固定第一个字符，排列后面的字符
                    string[begin], string[i] = string[i], string[begin]  # 记得换回来

        if not ss:
            return []
        result = []
        permutation(list(ss), 0)
        return sorted(list(set(result)))

    def Permutation2(self, ss):
        def permutation(string):
            if len(string) == 1:  # 只剩下一个字符时直接返回该字符
                return [string]
            result = []
            for i in range(len(string)):
                for j in permutation(string[:i] + string[i + 1:]):  # 从头到尾逐个字符抽出来，剩下字符的进行排列
                    result.append(string[i] + j)  # 把抽出来的那个字符与排列好的字符串拼在一起
            return result

        if not ss:
            return []
        return sorted(list(set(permutation(ss))))

    def Permutation3(self, ss):
        if not ss:
            return []
        return sorted(list(set(map(''.join, itertools.permutations(ss)))))


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append(['', []])
        testArgs.append(['a', ['a']])
        testArgs.append(['ab', ['ab', 'ba']])
        testArgs.append(['aa', ['aa']])
        testArgs.append(['abc', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

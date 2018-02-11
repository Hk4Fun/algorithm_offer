__author__ = 'Hk4Fun'
__date__ = '2018/2/11 15:53'

'''题目描述：
如果两个单词中出现的字母相同且每个字母出现的次数也相同，那么这两个单词互为变位词(Anagram)。
例如listen和silent、evil和live。请完成一个函数，判断输入的两个字符串是否为变位词。
'''
'''主要思路：
思路1：pythonic，利用python的set数据结构快速判断
思路2：将word1和word2建成两张哈希表，值为出现的次数，看两张表是否相等
'''


class Solution:
    def Anagram1(self, word1, word2):
        if word1 == None or word1 == None:
            return
        return set(word1) == set(word2)

    def Anagram2(self, word1, word2):
        if word1 == None or word1 == None:
            return
        d1 = {}
        d2 = {} # 这里不能d1 = d2 = {}，因为后面会改变字典，d1和d2将会一致

        for w1 in word1:
            if w1 not in d1.keys():
                d1[w1] = 1
            else:
                d1[w1] += 1
        for w2 in word2:
            if w2 not in d2.keys():
                d2[w2] = 1
            else:
                d2[w2] += 1
        return d1 == d2


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 互为变位词
        testArgs.append(['listen', 'silent', True])

        # 不互为变位词
        testArgs.append(['wood', 'wolf', False])

        # 单个字母
        testArgs.append(['a', 'a', True])
        testArgs.append(['a', 'b', False])

        # word1和word2均为空串
        testArgs.append(['', '', True])

        # word1和word2均为None
        testArgs.append([None, None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

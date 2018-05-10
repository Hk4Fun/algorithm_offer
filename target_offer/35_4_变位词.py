__author__ = 'Hk4Fun'
__date__ = '2018/2/11 15:53'

'''题目描述：
如果两个单词中出现的字母相同且每个字母出现的次数也相同，那么这两个单词互为变位词(Anagram)。
例如listen和silent、evil和live。请完成一个函数，判断输入的两个字符串是否为变位词。
'''
'''主要思路：
思路1：将word1和word2建成两张哈希表，记录出现的次数，看两张表是否相等
思路2: 思路2在空间上的优化。只需用word1建立一张表（在表上添加记录，做加法），
       而word2在这张表上查询并做减法，最后若表中所有键的值都为0，则说明为变位词，否则不是
'''


class Solution:

    def Anagram1(self, word1, word2):
        if word1 == None or word1 == None:
            return
        # 这里不能table1 = table1 = [0] * 26，因为后面会改变其中一个，另一个也会一起改变，因为列表的引用是同一个
        table1, table2 = [0] * 26, [0] * 26
        for char in word1:
            index = ord(char) - ord('a')
            table1[index] = table1[index] + 1
        for char in word2:
            index = ord(char) - ord('a')
            table2[index] = table2[index] + 1
        return table1 == table2

    def Anagram2(self, word1, word2):
        if word1 == None or word1 == None:
            return
        table = [0] * 26
        for char in word1:
            index = ord(char) - ord('a')
            table[index] = table[index] + 1
        for char in word2:
            index = ord(char) - ord('a')
            table[index] = table[index] - 1
        return table == [0] * 26


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

        testArgs.append(["aacc", "ccac", False])
        testArgs.append(['aa', 'a', False])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    MyTest(Solution()).start_test()

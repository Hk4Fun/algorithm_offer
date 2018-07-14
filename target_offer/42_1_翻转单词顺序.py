__author__ = 'Hk4Fun'
__date__ = '2018/2/15 17:12'

'''题目描述：
输入一个英文句子, 翻转句子中单词的顺序,但单词内字符的顺序不变
为简单起见, 标点符号和前面的单词属于同一个单词
'''
'''主要思路：
思路1：两次翻转，第一次整体翻转，第二次每个单词再翻转（也可以先每个单词翻转然后整体翻转）
思路2：从前往后一直读取，遇到空格之后就把之前读取到的单词放到结果的前面并在前面添上空格，
       最后读取的单词直接加在前面就行了
思路3：将整个句子以空格分开成各个单词，然后以单词为单位翻转，再以空格拼接
思路4：同思路1，但不用分片也不用split
'''


class Solution:
    def ReverseSentence1(self, s):
        return ' '.join(i[::-1] for i in s[::-1].split(' ')) if s != None else None

    def ReverseSentence2(self, s):
        if s != None:
            result = tmp = ''  # tmp临时存放每个单词
            for char in s:
                if char == ' ':
                    result = ' ' + tmp + result
                    tmp = ''
                else:
                    tmp += char
            result = tmp + result
            return result

    def ReverseSentence3(self, s):
        return ' '.join(s.split(' ')[::-1]) if s != None else None

    def ReverseSentence4(self, s):
        def reverse(s, start, end):
            if not s:
                return ''
            while start < end:
                s[start], s[end] = s[end], s[start]
                start += 1
                end -= 1
            return ''.join(s)

        if s != None:
            s = list(s)
            length = len(s)
            reverse(s, 0, length - 1)
            start = 0
            while start < length:
                while start < length and s[start] == ' ': start += 1
                end = start
                while end < length and s[end] != ' ': end += 1
                reverse(s, start, end - 1)
                start = end
            return ''.join(s)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 句子中有多个单词
        testArgs.append(['I am a student.', 'student. a am I'])

        # 句子中只有一个单词
        testArgs.append(['Wonderful', 'Wonderful'])

        # 字符串中只有空格
        testArgs.append([' ', ' '])

        # 空串
        testArgs.append(['', ''])

        # None
        testArgs.append([None, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

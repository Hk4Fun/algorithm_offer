__author__ = 'Hk4Fun'
__date__ = '2018/1/1 16:28'

'''题目描述：
请实现一个函数，将一个字符串中的空格替换成“%20”。
例如，当字符串为We Are Happy.则经过替换之后的字符串为We%20Are%20Happy。
'''
'''主要思路：
思路1：使用内置方法replace
思路2：创建新字符串，不需要移动替换位置之后的字符，所以可以从左到右扫描字符串，
       遇到空格直接写入‘20%’即可，其他情况下直接复制
思路3:原地替换，需要移动替换位置之后的字符，若从左到右扫描，一边移动一边替换，时间复杂度为O（n^2）
      可以考虑从右到左扫描，使用两个索引，一个指向源字符串的末尾P1，另一个指向替换后字符串的末尾P2，
      没碰到空格时直接复制，碰到空格时P2左移3格写入‘20%’，P1左移一格
      （每替换一个空格，长度增加2，因此替换后字符串的长度=原来长度+2*空格数目）
      注：如果是c/c++可以实现原地替换，但python中的str为不可变对象，只能返回新的字符串，
      所以这里的原地替换只是模拟书中的方法，实际上还是返回一个新的字符串
'''


class Solution:
    # s为源字符串
    def replaceSpace1(self, s):
        if type(s) != str:
            return
        return s.replace(' ', '%20')

    def replaceSpace2(self, s):
        if type(s) != str:
            return
        newStr = ''
        for char in s:
            if char == ' ':
                newStr += '%20'
            else:
                newStr += char
        return newStr

    def replaceSpace3(self, s):
        if type(s) != str:
            return
        originalLength = 0
        numberOfBlank = 0
        for char in s:
            originalLength += 1
            if char == ' ':
                numberOfBlank += 1
        newLength = originalLength + numberOfBlank * 2
        newStr = [None] * newLength  # 不能为字符串，因为后面要进行赋值原地修改
        indexOfOriginal, indexOfNew = originalLength - 1, newLength - 1  # 这里需要减一，因为python中字符串不用‘\0’结尾
        while indexOfOriginal >= 0 and indexOfNew > indexOfOriginal:
            if s[indexOfOriginal] == ' ':
                newStr[indexOfNew - 2:indexOfNew + 1] = ['%', '2', '0']
                indexOfNew -= 3
            else:
                newStr[indexOfNew] = s[indexOfOriginal]
                indexOfNew -= 1
            indexOfOriginal -= 1
        while indexOfOriginal >= 0:  # 将剩下的复制到新串
            newStr[indexOfNew] = s[indexOfOriginal]
            indexOfOriginal -= 1
            indexOfNew -= 1
        return ''.join(newStr)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        testArgs.append(['hello world', 'hello%20world'])  # 空格在句子中间
        testArgs.append([' helloworld', '%20helloworld'])  # 空格在句子开头
        testArgs.append(['helloworld ', "helloworld%20"])  # 空格在句子末尾
        testArgs.append(['hello  world', "hello%20%20world"])  # 连续有两个空格
        testArgs.append([None, None])  # 传入None
        testArgs.append(['', ''])  # 传入内容为空的字符串
        testArgs.append([' ', "%20"])  # 传入内容为一个空格的字符串
        testArgs.append(['helloworld', "helloworld"])  # 传入的字符串没有空格
        testArgs.append(['   ', "%20%20%20"])  # 传入的字符串全是空格

        return testArgs



if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

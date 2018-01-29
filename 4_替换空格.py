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
        indexOfOriginal, indexOfNew = originalLength - 1, newLength - 1 # 这里需要减一，因为python中字符串不用‘\0’结尾
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
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, methodType, string, expected):
    # methodType表示要测试的方法，
    # 1表示replaceSpace1， 2表示replaceSpace2，3表示1表示replaceSpace3

    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0

    try:
        if methodType == 1 or methodType == '1':
            start = timeit.default_timer()
            result = test.replaceSpace1(string)
            end = timeit.default_timer()
        elif methodType == 2 or methodType == '2':
            start = timeit.default_timer()
            result = test.replaceSpace2(string)
            end = timeit.default_timer()
        elif methodType == 3 or methodType == '3':
            start = timeit.default_timer()
            result = test.replaceSpace3(string)
            end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


# Test("Test1_1", 1, 'hello world', "hello%20world")  # 空格在句子中间
# Test("Test1_2", 1, ' helloworld', "%20helloworld")  # 空格在句子开头
# Test("Test1_3", 1, 'helloworld ', "helloworld%20")  # 空格在句子末尾
# Test("Test1_4", 1, 'hello  world', "hello%20%20world")  # 连续有两个空格
# Test("Test1_5", 1, None, None)  # 传入None
# Test("Test1_6", 1, '', '')  # 传入内容为空的字符串
# Test("Test1_7", 1, ' ', "%20")  # 传入内容为一个空格的字符串
# Test("Test1_8", 1, 'helloworld', "helloworld")  # 传入的字符串没有空格
# Test("Test1_9", 1, '   ', "%20%20%20")  # 传入的字符串全是空格
#
# Test("Test2_1", 2, 'hello world', "hello%20world")  # 空格在句子中间
# Test("Test2_2", 2, ' helloworld', "%20helloworld")  # 空格在句子开头
# Test("Test2_3", 2, 'helloworld ', "helloworld%20")  # 空格在句子末尾
# Test("Test2_4", 2, 'hello  world', "hello%20%20world")  # 连续有两个空格
# Test("Test2_5", 2, None, None)  # 传入None
# Test("Test2_6", 2, '', '')  # 传入内容为空的字符串
# Test("Test2_7", 2, ' ', "%20")  # 传入内容为一个空格的字符串
# Test("Test2_8", 2, 'helloworld', "helloworld")  # 传入的字符串没有空格
# Test("Test2_9", 2, '   ', "%20%20%20")  # 传入的字符串全是空格
#
Test("Test3_1", 3, 'hello world', "hello%20world")  # 空格在句子中间
Test("Test3_2", 3, ' helloworld', "%20helloworld")  # 空格在句子开头
Test("Test3_3", 3, 'helloworld ', "helloworld%20")  # 空格在句子末尾
Test("Test3_4", 3, 'hello  world', "hello%20%20world")  # 连续有两个空格
Test("Test3_5", 3, None, None)  # 传入None
Test("Test3_6", 3, '', '')  # 传入内容为空的字符串
Test("Test3_7", 3, ' ', "%20")  # 传入内容为一个空格的字符串
Test("Test3_8", 3, 'helloworld', "helloworld")  # 传入的字符串没有空格
Test("Test3_9", 3, '   ', "%20%20%20")  # 传入的字符串全是空格

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))

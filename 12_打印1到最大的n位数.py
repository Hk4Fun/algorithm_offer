__author__ = 'Hk4Fun'
__date__ = '2018/1/6 2:39'

'''题目描述：
输入数字n, 按顺序打印从1最大的n位十进制数，
比如输入3, 则打印出1、2、3、到最大的3位数即999
（这里不打印，而是返回一个list）
'''
'''主要思路：
由于没有位数限制，所以要考虑大数问题，用字符串或数组表示大数
需要注意的问题是字符串或者数组的最高位对于数字上的最低位
思路1：在字符串表达的数字上模拟加法，然后将字符串表达的数值打印出来
思路2：n位所有十进制其实就是n个从0到9的全排列（递归实现），只是在打印时前面多余的0不打印
'''


class Solution:
    def RmStartZero(self, number):  # 去掉前面多余的0
        if int(''.join(number)) == 0:  # 全0直接返回
            return number
        num = number[:]  # 拷贝，因为pop操作会修改number的长度
        while not int(num[0]):
            num.pop(0)
        return num

    def Print1ToMaxOfNDigits1(self, n):
        def Increment(number):
            isOverflow = False
            nTakeOver = 0
            nLength = len(number)

            for i in range(nLength - 1, -1, -1):
                nSum = int(number[i]) + nTakeOver
                if i == nLength - 1:
                    nSum += 1

                if nSum >= 10:
                    if i == 0:
                        isOverflow = True
                    else:
                        nSum -= 10
                        nTakeOver = 1
                        number[i] = str(nSum)
                else:
                    number[i] = str(nSum)
                    break

            return isOverflow

        if n <= 0:
            return
        l = []
        number = ['0'] * n
        while not Increment(number):
            l.append(''.join(self.RmStartZero(number)))
        return l

    def Print1ToMaxOfNDigits2(self, n):
        l = []

        def Print1ToMaxOfNDigitsRecursively(number, length, index):
            if index == length - 1:
                l.append(''.join(self.RmStartZero(number)))
                return
            for i in range(10):
                number[index + 1] = str(i)
                Print1ToMaxOfNDigitsRecursively(number, length, index + 1)

        if n <= 0:
            return
        number = ['0'] * n
        for i in range(10):
            number[0] = str(i)
            Print1ToMaxOfNDigitsRecursively(number, n, 0)
        return l[1:]  # 去掉第一个数值‘0’


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 总的测试数量
time_pool = []  # 耗时


def Test(testName, method_type, n, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0
    try:
        if method_type == 1:
            start = timeit.default_timer()
            result = test.Print1ToMaxOfNDigits1(n)
            end = timeit.default_timer()
        elif method_type == 2:
            start = timeit.default_timer()
            result = test.Print1ToMaxOfNDigits2(n)
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


Test('Test1_1', 1, 1, [str(i + 1) for i in range(9)])  # 正常功能测试
Test('Test1_2', 1, 2, [str(i + 1) for i in range(99)])  # 正常功能测试
Test('Test1_3', 1, 5, [str(i + 1) for i in range(99999)])  # 大数测试
Test('Test1_4', 1, 0, None)  # 鲁棒性，位数0
Test('Test1_5', 1, -1, None)  # 鲁棒性，位数为负数

Test('Test2_1', 2, 1, [str(i + 1) for i in range(9)])  # 正常功能测试
Test('Test2_2', 2, 2, [str(i + 1) for i in range(99)])  # 正常功能测试
Test('Test2_3', 2, 5, [str(i + 1) for i in range(99999)])  # 大数测试
Test('Test2_4', 2, 0, None)  # 鲁棒性，位数0
Test('Test2_5', 2, -1, None)  # 鲁棒性，位数为负数

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))

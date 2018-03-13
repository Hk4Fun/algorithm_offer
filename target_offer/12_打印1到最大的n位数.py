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

    def Print1ToMaxOfNDigits1(self, n):
        def RmStartZero(number):  # 去掉前面多余的0
            if int(''.join(number)) == 0:  # 全0直接返回
                return number
            num = number[:]  # 拷贝，因为pop操作会修改number的长度
            while not int(num[0]):
                num.pop(0)
            return num

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
            l.append(''.join(RmStartZero(number)))
        return l

    def Print1ToMaxOfNDigits2(self, n):
        def RmStartZero(number):  # 去掉前面多余的0
            if int(''.join(number)) == 0:  # 全0直接返回
                return number
            num = number[:]  # 拷贝，因为pop操作会修改number的长度
            while not int(num[0]):
                num.pop(0)
            return num

        l = []

        def Print1ToMaxOfNDigitsRecursively(number, length, index):
            if index == length - 1:
                l.append(''.join(RmStartZero(number)))
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
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        testArgs.append([1, [str(i + 1) for i in range(9)]])  # 正常功能测试
        testArgs.append([2, [str(i + 1) for i in range(99)]])  # 正常功能测试
        testArgs.append([5, [str(i + 1) for i in range(99999)]])  # 大数测试
        testArgs.append([0, None])  # 鲁棒性，位数0
        testArgs.append([-1, None])  # 鲁棒性，位数为负数

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

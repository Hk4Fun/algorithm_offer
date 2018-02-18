__author__ = 'Hk4Fun'
__date__ = '2018/2/18 17:10'

'''题目描述：
写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号
'''
'''主要思路：
思路1：位运算，
       1.两个数异或：相当于每一位相加，而不考虑进位；
       2.两个数相与，并左移一位：相当于求得进位；
       3.将上述两步的结果相加：相当于重复执行上述两步，直到不产生进位
       由于python的整型是无限位数的，所以有可能导致不断进位，所以需要截取后32位，即&0xffffffff
       但这样就会导致和为负数时由于截取使得结果为正数，所以需要检查一下如果结果的最高位为1，
       说明结果为负数，需要将最高位左边所有的0变为1，这样就可以变为负数，然后按照补码转换成正确的数值
       (无需进行补码转换，机器内部自动转换)。也就是说需要保持右边32位不变而左边所有位取反，
       所以可以先把右边32位局部取反，然后整体取反。局部取反可以^0xffffffff，而整体取反直接~
思路2（可以忽略）：使用sum()
'''


class Solution:
    def Add1(self, num1, num2):
        mask = 0xffffffff
        while num2:
            num1, num2 = (num1 ^ num2) & mask, ((num1 & num2) << 1) & mask
        return num1 if num1 >> 31 == 0 else ~(num1 ^ mask)

    def Add2(self, num1, num2):
        return sum([num1, num2])


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([1, 2, 3])
        testArgs.append([111, 899, 1010])
        testArgs.append([3, 0, 3])
        testArgs.append([1, -2, -1])
        testArgs.append([0, -4, -4])
        testArgs.append([-2, -8, -10])
        testArgs.append([-1, 1, 0])
        testArgs.append([-1, 2, 1])
        testArgs.append([-3, 4, 1])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

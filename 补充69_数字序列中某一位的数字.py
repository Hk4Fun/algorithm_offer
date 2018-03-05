__author__ = 'Hk4Fun'
__date__ = '2018/3/5 11:42'

'''题目描述：
数字按照0123456789101112131415161718192021…的顺序排列。
第5位（从0开始计数）为5，第13位为1，第19位为4…… 求任意第n位对应的数字。
'''
'''主要思路：
思路1：暴力枚举。每枚举一个数字的时候，求出该数字是几位数，并把数字的位数和前面的所有数字的位数相加。
       当累加的数位大于n时，那么第n位数字一定在这个数字里。
思路2：当然正确的思路是找出某些规律跳过若干数字。例如：序列前十位是0~9。
       接下来180位数字是90个10~99的两位数。接下来的2700位是900个100~999的三位数。即分组寻找，锁定范围
'''


class Solution:
    def digitAtIndex1(self, index):
        def countDigits(number):
            # 统计每个数的位数
            if number == 0:
                return 1
            count = 0
            while number:
                count += 1
                number //= 10
            return count

        if index == None or index < 0:
            return
        count = 0
        number = 0
        while True:
            count += countDigits(number)
            if count > index:
                for i in range(1, count - index):  # 右移
                    number //= 10
                return number % 10
            number += 1

    def digitAtIndex2(self, index):
        if index == None or index < 0:
            return
        digits = 1  # 表示位数
        while True:
            numbers = 10 if digits == 1 else 9 * (10 ** (digits - 1))  # digits位数字总共有多少个
            if index < numbers * digits:  # 在范围内
                number = (0 if digits == 1 else 10 ** (digits - 1)) + index // digits  # 求出落在哪个数上
                for i in range(1, digits - index % digits):  # 右移
                    number //= 10
                return number % 10
            index -= digits * numbers  # 还没在范围内则继续往后找
            digits += 1


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([0, 0])
        testArgs.append([1, 1])
        testArgs.append([9, 9])
        testArgs.append([10, 1])
        testArgs.append([189, 9])  # 数字99的最后一位，9
        testArgs.append([190, 1])  # 数字100的第一位，1
        testArgs.append([1000, 3])  # 数字370的第一位，3
        testArgs.append([1001, 7])  # 数字370的第二位，7
        testArgs.append([1002, 0])  # 数字370的第三位，0
        testArgs.append([None, None])
        testArgs.append([-1, None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

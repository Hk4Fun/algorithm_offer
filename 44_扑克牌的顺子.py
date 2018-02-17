__author__ = 'Hk4Fun'
__date__ = '2018/2/17 0:23'

'''题目描述：
从扑克牌中随机抽取5张牌，判断是不是顺子，即这5张牌是不是连续的。2~10为数字本身，A为1，J~K为11~13，
而大小王可以看成任意数字。为方便起见这里把大小王看成0，且规定含有对子时不为顺子。
注意：这里大小王的个数不限，且输入参数的AJQK和大小王已经转换成相应数字
'''
'''主要思路：
思路1：1. 除0外没有重复的数，2. max - min < 5 （由于max和min动态变化，但最终max-min=4）
思路2：首先排序数组，再统计数组中0的个数，最后统计排序数组中相邻数字之间的空缺总数。
       如果空缺的总数小于或者等于0的个数，那么这个数组就是连续的，反之不连续。
'''


class Solution:
    def IsContinuous1(self, numbers):
        if not numbers or len(numbers) != 5:
            return False
        # 把A、J、Q、K转化一下
        # transDict = {'A': 1, 'J': 11, 'Q': 12, 'K': 13}
        # for i in range(len(numbers)):
        #     if numbers[i] in transDict.keys():
        #         numbers[i] = transDict[numbers[i]]
        min = 14
        max = -1
        flag = 0  # 用位图来记录每个出现过的数字
        for i in range(len(numbers)):
            number = numbers[i]
            if number < 0 or number > 13: return False
            if number == 0: continue
            if ((flag >> number) & 1) == 1: return False  # 如果出现过，那么再次出现就是对子了
            flag |= (1 << number)  # 记录出现过的数字
            if number > max: max = number
            if number < min: min = number
            if max - min >= 5: return False
        return True

    def IsContinuous2(self, numbers):
        if not numbers or len(numbers) != 5:
            return False
        length = len(numbers)

        # 统计大小王的个数，并检查每个数是否有效（>=0and<=13）
        zero_num = 0
        for i in numbers:
            if i == 0:
                zero_num += 1
            elif i < 0 or i > 13:
                return False
        numbers.sort()
        # 统计相邻数字的空缺个数
        start = zero_num
        next = start + 1
        gap_num = 0
        while next < length:
            # 如果出现对子的情况，一定不可能成为顺子
            if numbers[next] == numbers[start]:
                return False
            gap_num += numbers[next] - numbers[start] - 1
            start = next
            next += 1
        # 判断能够成为顺子
        if gap_num <= zero_num:
            return True
        return False


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([[1, 3, 2, 5, 4], True])

        testArgs.append([[1, 3, 2, 6, 4], False])

        testArgs.append([[0, 3, 2, 6, 4], True])

        testArgs.append([[0, 3, 1, 6, 4], False])

        testArgs.append([[1, 3, 0, 5, 0], True])

        testArgs.append([[1, 3, 0, 7, 0], False])

        testArgs.append([[1, 0, 0, 5, 0], True])

        testArgs.append([[1, 0, 0, 7, 0], False])

        testArgs.append([[3, 0, 0, 0, 0], True])

        testArgs.append([[0, 0, 0, 0, 0], True])

        testArgs.append([[1, 0, 0, 1, 0], False])

        testArgs.append([[-1, 14, 2, 3, 4], False])

        testArgs.append([[0, 0, 0, 0, 0, 0], False])

        testArgs.append([[1, 2, 3, 4], False])

        testArgs.append([[], False])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

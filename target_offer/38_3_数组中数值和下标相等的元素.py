__author__ = 'Hk4Fun'
__date__ = '2018/3/5 22:31'

'''题目描述：
假设一个单调递增的数组里边的每个元素都是整数并且是唯一的。
请实现一个函数，找出数组中从左往右第一个数值等于其下标的元素。
例如在数组{-3,-1,1,3,5}中，数字3和它的下标相等
'''
'''主要思路：
思路1（时间O(n),空间O(1)）：
枚举。从头到尾一次扫描数组中的数字，逐一检验数字是否和下标相等

思路2（时间O(logn),空间O(1)）：
二分。由于数字唯一且单调递增，则
若中间数字的值大于其下标，那么它右边的数字都大于对应的下标，往左找；
若中间数字的值小于其下标，那么它左边的数字都小于对应的下标，往右找；
若中间数字的值等于其下标，且左边那个数小于对应的下标，则为第一个数值等于下标的元素，
否则左边那个数一定等于下标，往左找
'''


class Solution:
    def GetNumberSameAsIndex1(self, numbers):
        if not numbers:
            return -1
        for i, v in enumerate(numbers):
            if i == v:
                return v
        return -1

    def GetNumberSameAsIndex2(self, numbers):
        if not numbers:
            return -1
        length = len(numbers)
        left, right = 0, length - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if numbers[mid] > mid:
                right = mid - 1
            elif numbers[mid] < mid:
                left = mid + 1
            else:
                if mid == 0 or numbers[mid - 1] < mid - 1:  # 考虑特殊情况：第一个就是值与下标相等
                    return numbers[mid]
                else:
                    right = mid - 1
        return -1


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[-3, -1, 1, 3, 4, 5, 10, 11], 3])
        testArgs.append([[0, 1, 2, 5, 6], 0])
        testArgs.append([[-1, 0, 1, 2, 3, 5], 5])
        testArgs.append([[-1, 0, 1, 2, 5], -1])
        testArgs.append([[0], 0])
        testArgs.append([[10], -1])
        testArgs.append([[], -1])
        testArgs.append([None, -1])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

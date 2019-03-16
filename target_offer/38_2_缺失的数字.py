__author__ = 'Hk4Fun'
__date__ = '2018/3/5 16:34'

'''题目描述：
一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0~n-1之内。
在范围0~n-1范围内的n个数字中有且只有一个数字不在该数组中，请找出该数字。
'''
'''主要思路：
思路1（时间O(n),空间O(1)）：
最直观的方法，先用求和公式求出数字0~n-1的所有数字之和s1。
接着求出数组中所有数字的和s2。则那个不在数组中的数字就是s1-s2

思路2（时间O（n），空间O（1））:
位运算。这里有0~n-1共n个数字，而下标为0~n-2，所以可以补上一个n-1（作为下标参与异或运算），
然后把所有下标和对应的数字异或起来，这样缺失的那个数字就是异或结果
（不必担心是否排序，反正最后会被异或消掉，而缺失的那个数字对应的下标没被消掉）

思路3（时间O(logn),空间O(1)）：
二分法。由于已经排好序，那么数组中开始的一些数字与它们的下标相同。
如果不在数组中的那个数字即为m，则所有比m小的数字下标都与它们的值相同
且m为第一个数值与下标不相等的下标。因此问题转化为在排序数组中找出第一个值与下标不相等的元素
下面基于二分进行查找：
如果中间值和下标相等，那么下一轮在右边找；
如果中间值和下标不等且前面一个元素的值和它的下标相等，
则中间这个下标正好是第一个值与下标不相等的下标；
如果中间值和下标不等且前面一个元素的值和它的下标也不相等，则下一轮在左边找
'''


class Solution:
    def GetMissingNumber1(self, numbers):
        if not numbers:
            return -1
        n = len(numbers)
        return (((n + 1) * n) >> 1) - sum(numbers)

    def GetMissingNumber2(self, numbers):
        if not numbers: return -1
        missing = len(numbers)
        for i, v in enumerate(numbers):
            missing ^= i ^ v
        return missing

    def GetMissingNumber3(self, numbers):
        if not numbers:
            return -1
        length = len(numbers)
        left, right = 0, length - 1
        while left <= right:
            mid = left + ((right - left) >> 1)
            if numbers[mid] == mid:
                left = mid + 1
            else:
                if mid == 0 or numbers[mid - 1] == mid - 1:  # 考虑特殊情况一开始就不一样（缺0）
                    return mid
                right = mid - 1
        if left == length:  # 考虑特殊情况都一样（缺n）
            return length
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

        testArgs.append([[1, 2, 3, 4, 5], 0])  # 缺失的是第一个数字0
        testArgs.append([[0, 1, 2, 3, 4], 5])  # 缺失的是最后一个数字
        testArgs.append([[0, 1, 2, 4, 5], 3])  # 缺失的是中间某个数字0
        testArgs.append([[1], 0])  # 数组中只有一个数字，缺失的是第一个数字0
        testArgs.append([[0], 1])  # 数组中只有一个数字，缺失的是最后一个数字1
        testArgs.append([[], -1])  # 空数组
        testArgs.append([None, -1])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

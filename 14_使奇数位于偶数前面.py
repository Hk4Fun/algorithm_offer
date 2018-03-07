__author__ = 'Hk4Fun'
__date__ = '2018/1/6 17:57'

'''题目描述：
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''
'''主要思路：
思路1（时间复杂度O(n^2)，空间复杂度O(1)）：
       从头扫描，每遇到偶数就把该偶数挪到最后面。该算法类似于冒泡排序，
       是一种稳定排序，符合题目要求但时间复杂度O(n^2)
思路2（时间复杂度O(n)，空间复杂度O(n)）：
       首先统计奇数的个数i，然后新建一个等长数组，遍历原数组。设置两个指针，
       奇数从0开始复制，偶数从i开始（奇数末尾）。稳定排序，时间复杂度降下来了，
       但空间复杂度提高了。
思路3（时间复杂度O(n)，空间复杂度O(1)）：
       头尾两个指针，尾指针总是指向奇数，头指针后移，遇到偶数就和尾指针交换。
       然后尾指针前移直到遇到奇数停下，然后头指针继续后移遇到偶数交换。
       最后当尾指针在头指针前面时结束。该算法类似于快排, 
       但只是简单的满足了奇数在前,偶数在后, 奇数的顺序发生了改变，是一种不稳定的排序。
       虽然时间空间复杂度都达到了最佳，但明显不符合题目要求。
思路4（Pythonic，sorted()）：
       使用python内置方法sorted()。注意这个sorted方法是一种稳定排序，且可以设置
       key = lambda x：x&1，将所有偶数映射成0，奇数映射成1，再排序。
       同时设置reverse = True，这样奇数在前偶数在后（先映射再稳定排序，排序根据映射后的值）
思路5（时间复杂度O(n)，空间复杂度O(n)）：
       创建两个数组，一个用来放奇数，一个用来放偶数。
       遍历原数组，遇到奇数放进奇数组，偶数放进偶数组，最后把偶数组拼接在奇数组后面即可。
'''


class Solution:
    def reOrderArray1(self, array):
        length = len(array)
        evenNum = length - sum([i & 1 for i in array])  # 统计偶数个数
        i = 0
        while evenNum:
            if not array[i] & 1:  # 遇到偶数则冒泡到最后面
                for j in range(i + 1, length):
                    array[j - 1], array[j] = array[j], array[j - 1]
                evenNum -= 1  # 冒泡个数加一，等于偶数个数时结束，但i不加，因为已经往前挪了一位
            else:  # 遇到奇数就往后索引
                i += 1
        return array

    def reOrderArray2(self, array):
        length = len(array)
        evenBegin = sum([i & 1 for i in array])  # 统计奇数个数，为偶数开始位置
        oddBegin = 0  # 奇数开始位置
        newArray = [None] * length
        for i in range(length):
            if array[i] & 1:
                newArray[oddBegin] = array[i]
                oddBegin += 1
            else:
                newArray[evenBegin] = array[i]
                evenBegin += 1
        return newArray

    # def reOrderArray3(self, array):
    #     if len(array) == 1:
    #         return array
    #
    #     front = 0
    #     rear = len(array) - 1
    #     while front < rear:
    #         while front < rear and array[front] & 1 == 1:  # 向后移动头指针，直到它指向偶数
    #             front += 1
    #         while front < rear and array[rear] & 1 == 0:  # 向前移动尾指针，直到它指向奇数
    #             rear -= 1
    #         if front < rear:
    #             array[front], array[rear] = array[rear], array[front]
    #     return array

    def reOrderArray4(self, array):
        return sorted(array, key=lambda x: x & 1, reverse=True)

    def reOrderArray5(self, array):
        return [num for num in array if num & 1] + [num for num in array if not num & 1]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        testArgs.append([[1, 2, 3, 4, 5, 6], [1, 3, 5, 2, 4, 6]])  # 奇数偶数交替出现
        testArgs.append([[1, 3, 5, 2, 4, 6], [1, 3, 5, 2, 4, 6]])  # 所有奇数都在偶数前面
        testArgs.append([[2, 4, 6, 1, 3, 5], [1, 3, 5, 2, 4, 6]])  # 所有偶数都在奇数前面
        testArgs.append([[1, 3, 5, 7, 9, 11], [1, 3, 5, 7, 9, 11]])  # 只有奇数
        testArgs.append([[2, 4, 6, 8, 10], [2, 4, 6, 8, 10]])  # 只有偶数
        testArgs.append([[1], [1]])  # 只有一个奇数
        testArgs.append([[0], [0]])  # 只有一个偶数
        testArgs.append([[], []])  # 空数组

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

__author__ = 'Hk4Fun'
__date__ = '2018/3/24 22:36'
'''题目描述：
合并两个排序的整数数组A和B变成一个新的数组
'''
'''主要思路：
时间O（n），空间O（n）
从前往后比较，小的先复制到新数组
'''


class Solution:
    def mergeSortedArray(self, A, B):
        """
        @param A: sorted integer array A
        @param B: sorted integer array B
        @return: A new sorted integer array
        """
        i = j = 0
        lenA, lenB = len(A), len(B)
        C = []
        for _ in range(lenA + lenB):
            if i > lenA - 1:
                C.append(B[j])
                j += 1
            elif j > lenB - 1:
                C.append(A[i])
                i += 1
            elif A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        return C


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[1, 2, 3], [4, 5], [1, 2, 3, 4, 5]])
        testArgs.append([[4, 5], [1, 2, 3], [1, 2, 3, 4, 5]])
        testArgs.append([[1, 3, 5], [2, 4], [1, 2, 3, 4, 5]])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

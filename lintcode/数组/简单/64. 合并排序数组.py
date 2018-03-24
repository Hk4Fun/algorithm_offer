__author__ = 'Hk4Fun'
__date__ = '2018/3/24 22:25'
'''题目描述：
合并两个排序的整数数组A和B变成一个新的数组。
注意事项：
你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。
样例：
给出 A = [1, 2, 3, empty, empty], B = [4, 5]
合并之后 A 将变成 [1,2,3,4,5]
'''
'''主要思路：
时间O（n），空间O（1）
从后往前比较并复制到A中，大的先复制
'''


class Solution:
    def mergeSortedArray(self, A, m, B, n):
        """
        @param: A: sorted integer array A which has m elements, but size of A is m+n
        @param: m: An integer
        @param: B: sorted integer array B which has n elements
        @param: n: An integer
        @return: nothing
        """
        i, j = m - 1, n - 1  # 从后往前比较
        for k in range(m + n - 1, -1, -1):
            if i < 0:
                A[k] = B[j]
                j -= 1
            elif j < 0:
                A[k] = A[i]
                i -= 1
            elif A[i] >= B[j]:
                A[k] = A[i]
                i -= 1
            else:
                A[k] = B[j]
                j -= 1
        return A  # 题目不要求返回任何值，这里是为了测试方便才返回


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

        testArgs.append([[1, 2, 3, None, None], 3, [4, 5], 2, [1, 2, 3, 4, 5]])
        testArgs.append([[1, 2, 3, None, None], 3, [2, 3], 2, [1, 2, 2, 3, 3]])
        testArgs.append([[3, 4, 5, None, None], 3, [1, 2], 2, [1, 2, 3, 4, 5]])
        testArgs.append([[None, None], 0, [1, 2], 2, [1, 2]])

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

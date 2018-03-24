__author__ = 'Hk4Fun'
__date__ = '2018/3/25 0:04'
'''题目描述：
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:
You may assume that nums1 has enough space (size that is greater or equal to m + n) 
to hold additional elements from nums2. 
The number of elements initialized in nums1 and nums2 are m and n respectively.
'''
'''主要思路：
时间O（n），空间O（1）:
采取从后往前的思路（这里的nums1已经扩容）
'''


class Solution:
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: void Do not return anything, modify nums1 in-place instead.
    """

    def merge1(self, nums1, m, nums2, n):
        i, j = m - 1, n - 1  # 从后往前比较
        for k in range(m + n - 1, -1, -1):
            if i < 0:
                nums1[k] = nums2[j]
                j -= 1
            elif j < 0:
                nums1[k] = nums1[i]
                i -= 1
            elif nums1[i] >= nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        return nums1  # 题目不要求返回任何值，这里是为了测试方便才返回

    def merge2(self, nums1, m, nums2, n):
        # 上一种解法的简化版
        # 不用考虑nums2遍历完而nums1还没有遍历完的情况，
        # 因为这里是把nums2放进nums1，nums1的数已经在数组中了
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n > 0:  # nums1已经遍历完，而nums2还没有，直接复制进去
            nums1[:n] = nums2[:n]
        return nums1  # 题目不要求返回任何值，这里是为了测试方便才返回


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
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

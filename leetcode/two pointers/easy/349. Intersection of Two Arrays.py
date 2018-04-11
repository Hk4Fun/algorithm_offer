__author__ = 'Hk4Fun'
__date__ = '2018/4/11 20:27'
'''题目描述：
Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
'''
'''主要思路：
时间O（max(m+n, nlogn, mlogm)），空间O（n）
先给两个数组排序，然后用两个指针分别指向两个数组的开头，
然后比较两个数组的大小，把小的数字的指针向后移，
如果两个指针指的数字相等，那么看结果res是否为空，
如果为空或者是最后一个数字和当前数字不等的话，将该数字加入结果res中
'''


class Solution:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    def intersection1(self, nums1, nums2):
        return list(set(nums1) & set(nums2))

    def intersection2(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        res = []
        i = j = 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                if len(res) == 0 or res[-1] != nums1[i]:
                    res.append(nums1[i])
                i += 1
                j += 1
        return res


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

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

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

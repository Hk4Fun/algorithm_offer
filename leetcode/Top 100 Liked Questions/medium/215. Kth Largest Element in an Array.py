__author__ = 'Hk4Fun'
__date__ = '2018/8/11 18:22'
'''题目描述：
Find the kth largest element in an unsorted array. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Example 1:

Input: [3,2,1,5,6,4] and k = 2
Output: 5
Example 2:

Input: [3,2,3,1,2,4,5,5,6] and k = 4
Output: 4
Note: 
You may assume k is always valid, 1 ≤ k ≤ array's length.
'''
'''主要思路：
时间O（n），空间O（1）
https://leetcode.com/problems/kth-largest-element-in-an-array/discuss/60306/Python-different-solutions-with-comments-(bubble-sort-selection-sort-heap-sort-and-quick-sort).
target_offer/30_最小的K个数.py 思路1
基于partition的算法
'''


class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # def partition(self, nums, l, r):
        # 荷兰国旗算法，基于交换，这里是顺序
        # nums[r]为pivot，[0,low) < pivot，[low,l) >= pivot，[l,r)为未知区域
        #     low = l
        #     while l < r:
        #         if nums[l] < nums[r]:
        #             nums[l], nums[low] = nums[low], nums[l]
        #             low += 1
        #         l += 1 # 刚交换过来的数一定 >=pivot，l可以直接往右移
        #     nums[low], nums[r] = nums[r], nums[low] # 最后记得把pivot交换过来
        #     return low

        def partition(l, r):
            # 挖坑法，基于覆盖
            i, j = l, r
            pivot = nums[l]
            while i < j:
                while i < j and nums[j] < pivot: j -= 1  # 逆序
                if i < j:
                    nums[i] = nums[j]
                    i += 1
                while i < j and nums[i] > pivot: i += 1
                if i < j:
                    nums[j] = nums[i]
                    j -= 1
            nums[i] = pivot
            return i

        l, r = 0, len(nums) - 1
        while l <= r:
            idx = partition(l, r)
            if idx < k - 1:
                l = idx + 1
            elif idx > k - 1:
                r = idx - 1
            else:
                return nums[k - 1]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
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
    MyTest(Solution()).start_test()

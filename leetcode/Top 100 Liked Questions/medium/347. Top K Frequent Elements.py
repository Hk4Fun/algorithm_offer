__author__ = 'Hk4Fun'
__date__ = '2018/7/29 8:34'
'''题目描述：
Given a non-empty array of integers, 
return the k most frequent elements.

For example,
Given [1,1,1,2,2,3] and k = 2, return [1,2].

Note: 
You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), 
where n is the array's size.
'''
'''主要思路：
思路1：时间O（n），空间O（n）
hashtable + partition

思路2：时间O(nlogk) ，空间O（n+k）  
hashtable（dict） + maxheap（heapq）

思路3：
pythonic, one line solution
'''

from collections import Counter
from heapq import heapify, heappushpop


class Solution:
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    def topKFrequent1(self, nums, k):
        def partition(arr, l, r):
            pivot = arr[l]  # 选择首位作为枢轴
            while l < r:
                while l < r and arr[r] >= pivot: r -= 1
                arr[l] = arr[r]
                while l < r and arr[l] <= pivot: l += 1
                arr[r] = arr[l]
            arr[l] = pivot
            return l

        tmp = {}
        for num in nums:
            tmp[num] = tmp.setdefault(num, 0) + 1  # 快速建立hashtable
        items = list(tmp.items())
        l, r = 0, len(items) - 1
        while l <= r:
            idx = partition(items, l, r)
            if idx < k - 1:
                l = idx + 1
            elif idx > k - 1:
                r = idx - 1
            else:
                return [item[0] for item in items[:k]]

    def topKFrequent2(self, nums, k):
        tmp = {}
        for num in nums:
            tmp[num] = tmp.setdefault(num, 0) + 1
        items = list(tmp.items())
        queue = [(item[1], item[0]) for item in items[:k]]
        heapify(queue)  # O(k)
        for item in items[k:]:  # O((n-k)log(k))
            heappushpop(queue, (item[1], item[0]))
        return [item[1] for item in queue]

    def topKFrequent3(self, nums, k):
        return list(list(zip(*Counter(nums).most_common(k)))[0])


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

        testArgs.append([[1, 1, 1, 2, 2, 3], 2, [1, 2]])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

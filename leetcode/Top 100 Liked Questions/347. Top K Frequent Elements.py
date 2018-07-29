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
dict + partition

思路2：时间O(n + klogn) ，空间O（n）  
dict + heapq（maxheap）

思路3：
pythonic, one line solution
'''

from collections import Counter
from heapq import heapify, heappop


class Solution:
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """

    def topKFrequent1(self, nums, k):
        def partition(arr, l, r):
            i, j = l, r
            pivot = arr[l]
            while i < j:
                while i < j and arr[j][1] <= pivot[1]: j -= 1
                if i < j:
                    arr[i] = arr[j]
                    i += 1
                while i < j and arr[i][1] >= pivot[1]: i += 1
                if i < j:
                    arr[j] = arr[i]
                    j -= 1
            arr[i] = pivot
            return i

        tmp = {}
        for num in nums:
            tmp[num] = tmp.setdefault(num, 0) + 1  # 快速建立hashtable
        items = list(tmp.items())
        l, r = 0, len(items) - 1
        while l <= r:
            index = partition(items, l, r)
            if index < k - 1:
                l = index + 1
            elif index > k - 1:
                r = index - 1
            else:
                return [item[0] for item in items[:k]]

    def topKFrequent2(self, nums, k):
        tmp = {}
        for num in nums:
            tmp[num] = tmp.setdefault(num, 0) + 1
        tmp = [(-item[1], item[0]) for item in list(tmp.items())]
        heapify(tmp)  # O（n）
        res = []
        for i in range(k):  # O（klogn）
            res.append(heappop(tmp)[1])
        return res

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

__author__ = 'Hk4Fun'
__date__ = '2018/8/22 13:44'
'''题目描述：
Design a class to find the kth largest element in a stream. 
Note that it is the kth largest element in the sorted order, 
not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k 
and an integer array nums, which contains initial elements from the stream. 
For each call to the method KthLargest.add, 
return the element representing the kth largest element in the stream.

Example:

int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8
Note: 
You may assume that nums' length ≥ k-1 and k ≥ 1.
'''
'''主要思路：
维护一个最小堆，
当数据流的个数小于等于k时直接heappush，
当数据流的个数大于k时heappushpop
则堆中的数总是最大的k个数，且堆顶是这k个数中最小的，
因此堆顶就是最大的k个数中最小的那个，即第k大的数
'''
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

from heapq import heappush, heappushpop


class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.k = k
        self.heap = []
        for n in nums:
            if self.k > 0:
                heappush(self.heap, n)
                self.k -= 1
            else:
                heappushpop(self.heap, n)

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.k > 0:
            heappush(self.heap, val)
            self.k -= 1
        else:
            heappushpop(self.heap, val)
        return self.heap[0]


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

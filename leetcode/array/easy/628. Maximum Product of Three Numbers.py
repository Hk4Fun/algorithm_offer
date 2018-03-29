__author__ = 'Hk4Fun'
__date__ = '2018/3/29 22:08'
'''题目描述：
Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:
Input: [1,2,3]
Output: 6

Example 2:
Input: [1,2,3,4]
Output: 24
Note:
The length of the given array will be in range [3,104] and all elements are in the range [-1000, 1000].
Multiplication of any three numbers in the input won't exceed the range of 32-bit signed integer.
'''
'''主要思路：
思路1（时间O（nlogn），空间O（logn））：
先排序，然后选最大三个数相乘，这就结束了？注意题目说存在负数。。。
所以还有一种情况：选最小的两个数（可能为负数）和最大的数相乘，比如这样：
-100，-99，0，1，2，3

思路2（时间O（n），空间O（1））：
既然只需要最大的三个数和最小的两个数，那么就用堆了。。。
建堆O（n），而选最大最小是固定数，要么3logn要么2logn，所以最终就是O（n）

思路3（时间O（n），空间O（1））：
遍历数组，自己维护最大的三个数和最小的两个数
'''
import heapq


class Solution:
    def maximumProduct1(self, nums):
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximumProduct2_1(self, nums):
        a, b = heapq.nlargest(3, nums), heapq.nsmallest(2, nums)
        return max(a[0] * a[1] * a[2], b[0] * b[1] * a[0])

    def maximumProduct2_2(self, nums):  # 又是一行。。。
        return max(nums) * max(a * b for a, b in [heapq.nsmallest(2, nums), heapq.nlargest(3, nums)[1:]])

    def maximumProduct3(self, nums):
        min1 = min2 = float('inf')
        max1 = max2 = max3 = -float('inf')
        for num in nums:
            if num <= min1: # num <= min1 <= min2
                min2 = min1
                min1 = num
            elif num <= min2: # min1 < num <= min2
                min2 = num
            if num >= max1: # num >= max1 >= max2 >= max3
                max3 = max2
                max2 = max1
                max1 = num
            elif num >= max2: # max1 > num >= max2 >= max3
                max3 = max2
                max2 = num
            elif num >= max3: # max1 >= max2 > max >= max3
                max3 = num
        return max(min1 * min2 * max1, max1 * max2 * max3)


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

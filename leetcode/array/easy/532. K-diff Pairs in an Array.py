__author__ = 'Hk4Fun'
__date__ = '2018/3/28 20:10'
'''题目描述：
Given an array of integers and an integer k, 
you need to find the number of unique k-diff pairs in the array. 
Here a k-diff pair is defined as an integer pair (i, j), 
where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
Output: 2
Explanation: There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input, we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation: There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
'''
'''主要思路：

思路1（时间O（nlogn），空间O（1））：
先排序，然后双指针i=0，j=1
如果nums[i]+k<j,则i++
如果nums[i]+k>j,则j++
如果nums[i]+k=j,则count++，i++
i++时遇到相等的直接略过，避免重复计算，同时保证j>i

思路2（时间O（n），空间O（n））：
先用字典哈希或collections.Counter(nums)
分三种情况：
k<0：return 0
k>0：检查字典中每个键+k是否也在字典里，是的话count++
k=0：相当于求出现次数两次以上的数字
'''

from collections import Counter


class Solution:
    def findPairs1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0: return 0
        nums.sort()
        count = 0
        i, j = 0, 1
        while j < len(nums):
            if j <= i or nums[i] + k > nums[j]:
                j += 1
            elif (i > 0 and nums[i] == nums[i - 1]) or (nums[i] + k < nums[j]):
                i += 1
            else:
                count += 1
                i += 1
        return count

    def findPairs2(self, nums, k):
        if k < 0:
            return 0
        elif k > 0:
            return len(set(nums) & {n + k for n in nums})
        else:
            return sum(v > 1 for v in Counter(nums).values())

    def findPairs3(self, nums, k):
        # 上一思路的简化版，不用set，但从测试结果来看效率变低了。。。
        d = Counter(nums)
        return sum(k > 0 and i + k in d or k == 0 and d[i] > 1 for i in d)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 10000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[1, 2, 3, 4, 5], 2, 3])
        testArgs.append([[6, 7, 3, 6, 4, 6, 3, 5, 6, 9], 4, 2])
        testArgs.append([[1, 1, 1, 1], -1, 0])
        testArgs.append([[1, 3, 1, 5, 4], 0, 1])

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

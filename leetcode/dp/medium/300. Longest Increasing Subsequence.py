__author__ = 'Hk4Fun'
__date__ = '2018/4/7 13:52'
'''题目描述：
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. 
Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?
'''
'''主要思路：
思路1（时间O（n^2），空间O（n））：
经典dp解法，但TLE了

思路2（时间O（nlogn），空间O（n））：带二分查找的dp
dp[i]代表长度为（i+1）的递增子序列中最小末尾子序列的末尾数字，比如nums = [4,5,6,3]，则
len = 1  :  [4], [5], [6], [3]   => dp[0] = 3
len = 2  :  [4, 5], [5, 6]       => dp[1] = 5
len = 3  :  [4, 5, 6]            => dp[2] = 6
易知dp是递增的，因此可以用二分查找来找到dp中应该更新的位置。
从左到右扫描nums，对于每个数字num，只执行下面两步中的一步：
(1) 如果num大于dp中最后一个数，则新增dp：dp.append(num)
(2) 如果dp[i-1] < num <= dp[i]，则更新dp[i]: dp[binarySearch(dp, num)] = num
最终len(dp)为最长递增子序列长度

下面说明为什么这样做是正确的：
当dp[i-1] < num <= dp[i]时，对于dp[i-1] < num，
则长度为i且以dp[i-1]为结尾的递增子序列必定可以在末尾添加num而加入到长度为i的递增子序列集合中，
此时又因为num <= dp[i]，所以长度为i的递增子序列集合中最小末尾子序列的末尾数字将被更新为num。
所以当num大于dp中最后一个数时，意味着num大于dp所有的数，所以num将产生len(dp)+1的新的长度的递增子序列：
只需在长度为len(dp)的最小末尾子序列后添加num。因此最终dp的长度就是整个数组能形成的最长递增子序列长度。
'''


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_binarySearch(self, nums):
        def binarySearch(nums, target):
            """返回刚好大于等于target的下标"""
            l, r = 0, len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m  # r 总是停留在大于等于target的位置上
                else:
                    l = m + 1  # l 不断向 r 靠近
            return l  # 最终 l == r, 停留在大于等于target的位置上

        if not nums: return 0
        dp = [nums[0]]
        for num in nums[1:]:
            if num > dp[-1]:
                dp.append(num)
            elif num < dp[-1]:
                dp[binarySearch(dp, num)] = num
            # 等于 dp[-1] 时会更新dp[-1]，多此一举，跳过
        return len(dp)


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 100  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[10, 9, 2, 5, 3, 7, 101, 18], 4])

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

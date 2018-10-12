__author__ = 'Hk4Fun'
__date__ = '2018/8/21 17:28'
'''题目描述：
Given an array of non-negative integers, 
you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
'''
'''主要思路：
解题思路历程（从回溯到动态规划到贪婪）：https://leetcode.com/problems/jump-game/solution/
该解题思路历程展示了如何一步一步优化，且从本质出发，授之以渔

最优解法（时间O（n），空间O（1））：贪婪
从右边往左边看，我们为了能够到达最右的位置（last = len(nums) - 1）
我们只需看左边是否有能够到达last的位置i
为此考虑当前位置（i）加上步数（nums[i]）是否超过 last 即可，
超过就说明一定能够到达（贪婪之处），因为 nums[i] 表示的步数是允许跳跃的最大步数
如果该位置i能到达last，那我们就更新last为i
因为我们只要能到达i就一定能够到达last，以此类推不断往左更新last；
如果该位置i不能到达last，就继续往左看不更新last，
因为该位置不能到达last并不意味着左边的i不能达到last
而只要一个位置能够到达last，我们就更新last，这也是贪婪之处
最后只需判断last是否为0即可，意味着只要我们从0号位置出发就一定能到达最右边
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: bool
    """

    def canJump(self, nums):
        if nums is None or len(nums) < 2: return True
        last = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last == 0


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

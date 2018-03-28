__author__ = 'Hk4Fun'
__date__ = '2018/3/28 19:07'
'''题目描述：
Given a binary array, find the maximum number of consecutive 1s in this array.

Example 1:
Input: [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s.
The maximum number of consecutive 1s is 3.

Note:
The input array will only contain 0 and 1.
The length of input array is a positive integer and will not exceed 10,000
'''
'''主要思路：
思路1：时间O（n），空间O（1）
从左到右遍历数组，遇到1计数加一，遇到0停止计数，比较最大值，然后把计数置0，
最后返回时记得再次比较最大值，因为可能结束了还没遇到0使得最大值一直得不到更新
思路2：时间O（n），空间O（1）
为了不在最后返回时再次比较最大值，可以在遇到1时计数加一然后就比较最大值，
遇到0计数置0就可以了。这对于0比1多有利，而如果1比0多还是采用思路1好
思路3：pythonic
一行解决。。。但效率堪忧
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """

    def findMaxConsecutiveOnes1(self, nums):
        count = maxSum = 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                maxSum = max(maxSum, count)
                count = 0
        return max(maxSum, count)

    def findMaxConsecutiveOnes2(self, nums):
        count = maxSum = 0
        for num in nums:
            if num == 1:
                count += 1
                maxSum = max(maxSum, count)
            else:
                count = 0
        return maxSum

    def findMaxConsecutiveOnes3(self, nums):
        return max(len(j) for j in ''.join(str(i) for i in nums).split('0'))


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

        testArgs.append([[1, 1, 0, 1, 1, 1], 3])
        testArgs.append([[1, 0, 1, 0, 1, 0], 1])
        testArgs.append([[0, 0, 0, 1], 1])
        testArgs.append([[1, 1, 1, 1, 1, 1, 1], 7])  # 有利于思路1
        testArgs.append([[0, 0, 0, 0, 0, 0, 0], 0])  # 有利于思路2

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

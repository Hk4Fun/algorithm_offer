__author__ = 'Hk4Fun'
__date__ = '2018/8/6 12:08'
'''题目描述：
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), 
prove that at least one duplicate number must exist. 
Assume that there is only one duplicate number, 
find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, 
but it could be repeated more than once.
'''
'''主要思路：
思路1（时间O（n），空间O（1））：
target_offer/51_数组中重复的数字.py 思路1

思路2（时间O（n），空间O（n））：
target_offer/51_数组中重复的数字.py 思路2
使用集合缓存出现过的数字

思路3（时间O（n），空间O（1））：
思路1修改了原数组，不符合题意，因此采用 Floyd 判圈算法：
从下标0出发，值作为next指针指向下一个下标，因此该数组可看做一个链表
又因为有重复的数字，因此会出现环，于是该题转化为寻找环的入口点
注意到数组中数值范围为1~n，因此下标0一定不会出现在环中，
所以可以把下标0作为链表的头结点开始遍历
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """

    def findDuplicate1(self, nums):
        i = 0
        while i < len(nums):
            idx = nums[i]
            if i == idx:
                i += 1
            elif nums[i] == nums[idx]:
                return nums[i]
            else:  # 只是交换，i不移动，因为交换过来的数还未检测
                nums[i], nums[idx] = nums[idx], nums[i]

    def findDuplicate2(self, nums):
        seen = set()
        for num in nums:
            if num in seen: return num
            seen.add(num)

    def findDuplicate3(self, nums):
        fast = slow = 0
        while True:
            fast = nums[nums[fast]]  # 走两步
            slow = nums[slow]  # 走一步
            if fast == slow:  # 来到相遇点
                fast = 0  # 一个从头出发，一个从相遇点出发
                while True:
                    fast, slow = nums[fast], nums[slow]  # 走一步
                    if fast == slow:  # 再次相遇
                        return slow  # 即为环入口点


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

        testArgs.append([[1, 3, 4, 2, 2], 2])
        testArgs.append([[3, 1, 3, 4, 2], 3])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

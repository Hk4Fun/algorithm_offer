__author__ = 'Hk4Fun'
__date__ = '2018/8/20 15:47'
'''题目描述：
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
'''
'''主要思路：
时间O（logn），空间O（1）
定义：旋转后数组被分为两个有序的子数组，如果target和nums[mid]在同一个子数组我们就说它在同边
logn必须采用二分：

s = (nums[mid] >= nums[0]) ^ (target >= nums[0])
当 s == 1 时，异边；s == 0 时，同边

如果target和nums[mid]同边，则正常二分：
若nums[mid] > target，则：hi = mid - 1
若nums[mid] < target，则：lo = mid + 1
否则： return mid

如果target和nums[mid]不同边，则：
若nums[mid] > target，则：lo = mid + 1（mid在左边子数组，target在右边子数组，mid左边的一定都比target大）
若nums[mid] < target，则：hi = mid - 1（mid在右边子数组，target在左边子数组，mid右边的一定都比target小）
否则：return mid
'''


class Solution:
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """

    def search(self, nums, target):
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid = (lo + hi) // 2
            if (nums[mid] >= nums[0]) ^ (target >= nums[0]):  # nums[mid] 和 target 不同边，注意这里的等号
                if nums[mid] > target:
                    lo = mid + 1
                elif nums[mid] < target:
                    hi = mid - 1
                else:
                    return mid
            else:  # 同边
                if nums[mid] > target:
                    hi = mid - 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    return mid
        return -1


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

        testArgs.append([[1, 3], 3, 1])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

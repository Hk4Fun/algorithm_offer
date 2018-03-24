__author__ = 'Hk4Fun'
__date__ = '2018/3/24 19:25'
'''题目描述：
Given an array and a value, remove all instances of that value in-place and return the new length.
Do not allocate extra space for another array, 
you must do this by modifying the input array in-place with O(1) extra memory.
The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:
Given nums = [3,2,2,3], val = 3,
Your function should return length = 2, with the first two elements of nums being 2.
'''
'''主要思路：
思路1（时间O（n），空间O（1））：
双指针，思路和上一题差不多，只不过现在数组不是有序的，但值是给定的

思路2（时间O（n），空间O（1））：
注意到，当 nums=[1,2,3,5,4],val=4 时，前面4个元素都发生了复制；
又如 nums=[4,1,2,3,5],val=4，后面四个元素都左移也发生了复制。
思路1是在不相等时发生复制，这对val重复个数少时不利，
所以当val重复个数少时，我们希望在不相等时只是移动指针，相等时才复制：
还是双指针，但这次一前一后相向移动而不是同方向：i在前面，j在后面。
当nums[i]==val时，nums[i]=nums[j]，发生复制，j--而i不动，因为i上的数是新复制过来的，待定；
当nums[i]!=val时，i++而j不动，不发生复制；
最后i>j时结束，返回i
注意到这样会打乱数组顺序，但题目允许这样做
'''


class Solution:
    def removeElement1(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:  # 注意这里是先复制再移动
                nums[i] = nums[j]
                i += 1
        return i

    def removeElement2(self, nums, val):
        i, j = 0, len(nums) - 1
        while i <= j:
            if nums[i] == val:
                nums[i] = nums[j]
                j -= 1
            else:
                i += 1
        return i


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

        testArgs.append([[3, 2, 2, 3], 3, 2])
        testArgs.append([[1], 1, 0])
        testArgs.append([[2], 1, 1])
        testArgs.append([[2, 2], 2, 0])
        testArgs.append([[], 0, 0])
        testArgs.append([[1, 2, 3], 4, 3])

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

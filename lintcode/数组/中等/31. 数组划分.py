__author__ = 'Hk4Fun'
__date__ = '2018/3/28 17:47'
'''题目描述：
给出一个整数数组 nums 和一个整数 k。划分数组（即移动数组 nums 中的元素），使得：
所有小于k的元素移到左边
所有大于等于k的元素移到右边
返回数组划分的位置，即数组中第一个位置 i，满足 nums[i] 大于等于 k。

注意事项：
你应该真正的划分数组 nums，而不仅仅只是计算比 k 小的整数数，
如果数组 nums 中的所有元素都比 k 小，则返回 nums.length。
'''
'''主要思路：
时间O（n），空间O（1）
荷兰国旗的简化版，只分两个区间，把大于区间和等于区间合并了
荷兰国旗问题归根到底就是双指针问题
'''


class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """

    def partitionArray(self, nums, k):
        l = 0  # l左边的数都比k小
        for i in range(len(nums)):
            if nums[i] < k:
                nums[l], nums[i] = nums[i], nums[l]
                l += 1
        return l


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

        testArgs.append([[3, 2, 2, 1], 2, 1])
        testArgs.append([[1, 1, 1, 1, 1], 3, 5])  # k比数组中的数都大
        testArgs.append([[3, 3, 3, 3, 3], 1, 0])  # k比数组中的数都小

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

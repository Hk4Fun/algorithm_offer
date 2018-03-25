__author__ = 'Hk4Fun'
__date__ = '2018/3/25 16:32'
'''题目描述：
Given an array of integers that is already sorted in ascending order, 
find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, 
where index1 must be less than index2. 
Please note that your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
'''
'''主要思路：
target_offer 41_1_和为s的两个数字

思路1（时间O（n），空间O（1））：双指针

思路2（时间O（n），空间O（n））：字典（哈希表）

思路3（时间O（nlogn），空间O（1））：二分查找

'''


class Solution:
    def twoSum_towPointer(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        l, r = 0, len(numbers) - 1
        while l <= r:
            if numbers[l] + numbers[r] < target:
                l += 1
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                return [l + 1, r + 1]

    def twoSum_dict_1(self, numbers, target):
        d = {}
        for i, v in enumerate(numbers):
            if v in d:
                return [d[v] + 1, i + 1]
            d[target - v] = i

    def twoSum_dict_2(self, numbers, target):
        # 用异常来检查是否存在
        d = {}
        for i, v in enumerate(numbers):
            try:
                return [d[v] + 1, i + 1]
            except KeyError:
                d[target - v] = i

    def twoSum_binary(self, numbers, target):
        for i in range(len(numbers)):
            l, r = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while l <= r:
                mid = l + (r - l) // 2
                if numbers[mid] < tmp:
                    l = mid + 1
                elif numbers[mid] > tmp:
                    r = mid - 1
                else:
                    return [i + 1, mid + 1]


# ================================测试代码===============================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 100  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        # 存在和为s的两个数字，这两个数字位于数组的中间
        testArgs.append([[1, 2, 5, 5, 11, 15], 10, [3, 4]])

        # 存在和为s的两个数字，这两个数字位于数组的两端
        testArgs.append([[1, 2, 4, 7, 11, 16], 17, [1, 6]])

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

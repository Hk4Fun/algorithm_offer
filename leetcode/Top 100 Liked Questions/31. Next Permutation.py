__author__ = 'Hk4Fun'
__date__ = '2018/10/27 17:29'
'''题目描述：
Implement next permutation, which rearranges numbers into 
the lexicographically next greater permutation of numbers.
If such arrangement is not possible, 
it must rearrange it as the lowest possible order (ie, sorted in ascending order).
The replacement must be in-place and use only constant extra memory.
Here are some examples.
Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1
'''
'''主要思路：
思路：时间O（n），空间O（1）
1.从后向前查看逆序区域，找到逆序区域的前一位k，也就是数字置换的边界
2.把逆序区域的前一位k和逆序区域中刚刚大于它的数字（从后往前第一个大于k的数）交换位置
3.把逆序区域逆序转为顺序
解释：
若给定1,2,3,4,5这几个数字，则最大的排列为54321，最小的排列为12345，可以发现顺序最小，逆序最大
为了找到下一个排列数，我们需要尽量保持高位不变，低位在最小的范围内变换顺序
那么，究竟需要变换多少位呢？这取决于当前整数的逆序区域
12354的逆序区域为[54]，仅看这两位已经是当前的最大组合
若想最接近原数，又比原数更大，必须从逆序区域的前一个数开始变换，这里是3
把下一个比它大的数字换过来，由于我们尽量保持高位不变，因此只能从后面的逆序区中找
于是我们从后面的逆序区域中寻找刚刚大于3的数字，和3的位置进行互换
这里有个技巧，我们从后往前找，第一个比3大的数就是逆序区中刚好大于3的数，这里是4
因为这是逆序区，再往前找只会比3更大
交换后逆序区仍然保持逆序（因为和3交换的数左边大于等于3，右边小于等于3），是逆序区最大的排列
于是12354变为12453，我们需要把逆序区反转一下调整为顺序，
这样就能让逆序区最小，得到下一个排列数，即12435
注意：如果逆序区是整个数串，说明已经是最后一个排列数了，
则不必发生交换操作，按照题意直接逆反转整个逆序区即可
'''


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        def find_idx():
            """从后往前找到逆序区的左边界idx，即nums[idx:]为逆序区，O(n)"""
            for i in range(len(nums) - 1, 0, -1):
                if nums[i] > nums[i - 1]:
                    return i
            return 0

        def exch(idx):
            """把逆序区的前一个数与逆序区刚好大于它的数交换"""
            for i in range(len(nums) - 1, idx - 1, -1):
                if nums[i] > nums[idx - 1]:
                    nums[idx - 1], nums[i] = nums[i], nums[idx - 1]
                    break

        def reverse(start):
            """将nums[start:]原地反转"""
            i, j = start, len(nums) - 1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        if not nums: return []  # for test
        idx = find_idx()
        if idx != 0:  exch(idx)  # 逆序区不是整个数串时需要多做一次交换
        reverse(idx)
        return nums  # for test


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

        from itertools import permutations
        for i in range(1, 6):
            nums = list(map(list, permutations(range(i)))) + [list(range(i))]
            for j in range(len(nums) - 1):
                testArgs.append([nums[j], nums[j + 1]])
        testArgs.append([[], []])
        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

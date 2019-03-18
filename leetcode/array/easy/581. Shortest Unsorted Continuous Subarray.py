__author__ = 'Hk4Fun'
__date__ = '2018/3/29 1:37'
'''题目描述：
Given an integer array, you need to find one continuous subarray 
that if you only sort this subarray in ascending order, 
then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order 
to make the whole array sorted in ascending order.
Note:
Then length of the input array is in range [1, 10,000].
The input array may contain duplicates, so ascending order here means <=.
'''
'''主要思路：
思路1（时间O（nlogn），空间O（n））：
1、将数组a排序到新的数组b
2、从左到右比较a和b，找到第一个不相等的数的下标beg
3、从右到左比较a和b，找到第一个不相等的数的下标end
4、end - beg + 1
注意：end必须始终大于beg

思路2（时间O（n），空间O（n））：
使用栈来完成：
https://leetcode.com/problems/shortest-unsorted-continuous-subarray/solution/
Approach #4 Using Stack [Accepted]

思路3（时间O（n），空间O（1））：
1、从左到右找到首次下降的下标beg（比如6,5，则6是beg）
2、从右到左找到首次上升的下标end（比如6,5，则5是end）
3、在nums[beg: (end + 1)]之间找到max和min
4、beg后退，来到首个比min小的数
5、end后退，来到首个比max大的数
6、end - beg - 1

思路4（时间O（n），空间O（1））：
最优解，是思路3的简化版
可以一边找max一边更新end：
从左到右看当前数是否大于等于max，是的话更新max，否则更新end（end是下标），
等于的情况下max和end都不更新
min和beg同理：
从右到左看当前数是否大于等于min，是的话更新min，否则更新beg（beg是下标）
等于的情况下min和beg都不更新
最终end来到这样一个位置：
它的左边存在比它还大的数，而右边都大于等于它，
且end不能再往右了，再往右则左边就不存在比它大的数了
beg同理：
它的右边存在比它还小的数，而左边都小于等于它，
且beg不能再往左了，再往左则右边就不存在比它小的数了
返回end - beg + 1
这里有一个特殊情况：
如果数组一开始就排好序的，max和min一直在更新，beg和end不会得到更新，
此时应该返回0，所以只要 end - beg + 1 == 0 即可，可设beg初值为-1,end初值为-2

从左到右和从右到左可以压缩在一个循环里完成

思路5：pythonic，基于思路1
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: int
    """

    def findUnsortedSubarray1(self, nums):
        sort = sorted(nums)
        beg, end = 0, len(nums) - 1
        while beg < len(nums) and nums[beg] == sort[beg]: beg += 1
        while end > beg and nums[end] == sort[end]: end -= 1
        return end - beg + 1

    def findUnsortedSubarray2(self, nums):
        stack = []
        beg = len(nums)
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                beg = min(beg, stack.pop())
            stack.append(i)
        stack = []
        end = 0
        for i in range(len(nums) - 1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)
        return end - beg + 1 if end > beg else 0

    def findUnsortedSubarray3(self, nums):
        beg, end = 0, len(nums) - 1
        while beg < len(nums) - 1 and nums[beg] <= nums[beg + 1]: beg += 1
        if beg == len(nums) - 1: return 0  # 已经排好序，直接返回0
        while end > 0 and nums[end] >= nums[end - 1]: end -= 1
        minV, maxV = min(nums[beg:(end + 1)]), max(nums[beg:(end + 1)])
        while beg >= 0 and nums[beg] > minV: beg -= 1
        while end <= len(nums) - 1 and nums[end] < maxV: end += 1
        return end - beg - 1

    def findUnsortedSubarray4(self, nums):
        beg, end = -1, -2
        maxV, minV = -float('inf'), float('inf')
        for i in range(len(nums)):
            if nums[i] >= maxV:
                maxV = nums[i]
            else:
                end = i
            if nums[-i - 1] <= minV:
                minV = nums[-i - 1]
            else:
                beg = len(nums) - i - 1
        return end - beg + 1

    def findUnsortedSubarray5(self, nums):  # pythonic
        is_same = [a == b for a, b in zip(nums, sorted(nums))]
        return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)

    def findUnsortedSubarray6(self, nums):  # pythonic,一句话解决。。。
        return len(''.join(('.', ' ')[a == b] for a, b in zip(nums, sorted(nums))).strip())


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

        testArgs.append([[2, 6, 4, 8, 10, 9, 15], 5])
        testArgs.append([[1, 2, 3, 4, 5, 6], 0])
        testArgs.append([[6, 5, 4, 3, 2, 1], 6])
        testArgs.append([[1, 2, 3, 3, 3], 0])

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

__author__ = 'Hk4Fun'
__date__ = '2018/2/20 17:41'

'''题目描述：
在一个长度为n的数组里的所有数字都在0到n-1的范围内。
数组中某些数字是重复的，但不知道有几个数字是重复的。也不知道每个数字重复几次。
请找出数组中重复的数字，没有则返回-1。
例如，如果输入长度为7的数组{2,3,1,0,2,5,3}，那么对应的输出是重复的数字2或者3。
'''
'''主要思路：
思路1（时间O(n), 空间O(1)）：
       由于长度为n的数组里的所有数字都在0到n-1的范围内，所以如果没有重复数字的话，
       那么从小到大排序后的数组每个数和它的下标应该是相等的。所以我们只需从头遍历数组，
       看每个数字和它下标是否相等，相等就遍历下一个，不相等就和它应该在的位置上
       （下标和它相等）的数字交换，交换前先检查一下如果那个数字和它相等那么就找到了重复数字了，
       没有必要交换，遍历下一个。
思路2（时间O(n), 空间O(n)）：
       使用集合缓存出现过的数字

'''


class Solution:
    # 返回重复数字的列表，没有直接返回-1
    def duplicate1(self, nums):
        if not nums: return -1
        i, res = 0, []
        while i < len(nums):
            idx = nums[i]
            if i == idx:
                i += 1
            elif nums[i] == nums[idx]:
                res.append(nums[i])
                i += 1
            else:  # 只是交换，i不移动，因为交换过来的数还未检测
                nums[i], nums[idx] = nums[idx], nums[i]
        return res if res else -1

    def duplicate2(self, nums):
        if not nums: return -1
        seen = set()
        res = []
        for num in nums:
            if num in seen:
                res.append(num)
            seen.add(num)
        return res if res else -1


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        self.debug = Test
        testArgs = []

        # 重复数字是最小的数字
        testArgs.append([[2, 1, 3, 1, 4], {1}])

        # 重复数字是最大的数字
        testArgs.append([[2, 4, 3, 1, 4], {4}])

        # 多个重复数字
        testArgs.append([[2, 4, 2, 1, 4], {2, 4}])

        # 没有重复数字
        testArgs.append([[2, 1, 3, 0, 4], -1])

        # 空数组
        testArgs.append([[], -1])

        # None
        testArgs.append([None, -1])

        return testArgs

    def convert(self, result, *func_arg):
        return set(result) if result != -1 else result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

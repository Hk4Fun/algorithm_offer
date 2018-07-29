__author__ = 'Hk4Fun'
__date__ = '2018/7/29 12:18'
'''题目描述：
Given a set of distinct integers, nums, 
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''
'''主要思路：
思路1：递归，target_offer/28_2_字符串的组合.py 思路2
思路2：迭代，每一次迭代都在前面所有结果上添加新的数字，如 
       [], 
       [1], 
       [2], [1,2]，
       [3], [1,3], [2,3], [1,2,3]
思路3：位运算
        321   
        000   []
        001   [3]
        010   [2]
        011   [2,3]
        100   [1]
        101   [1,3]
        110   [1,2]
        111   [1,2,3]
思路4：位运算，综合运用两个位运算技巧：
        n & (n - 1)：去掉最右边的1
        n & -n：取出最右边的1
        n = [n & (n - 1)] + [n & -n] = n & [n - 1 - n] = n & -1 = n
'''


class Solution:
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """

    def subsets1(self, nums):
        def sub(nums):
            if not nums: return []
            res = []
            for i, n in enumerate(nums):
                res.append([n])
                for p in sub(nums[i + 1:]):
                    res.append([n] + p)
            return res

        return [[]] + sub(nums)

    def subsets2(self, nums):
        res = [[]]
        for i, n in enumerate(nums):
            # for r in res[:len(res)]:
            #     res.append([n] + r)
            res += [[n] + r for r in res]
        return res

    def subsets3(self, nums):
        res = []
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                if (1 << j) & i:
                    tmp.append(nums[j])
            res.append(tmp)
        return res

    def subsets3_oneline(self, nums):
        return [[num for i, num in enumerate(nums) if (1 << i) & mask]
                for mask in range(1 << len(nums))]

    def subsets4(self, nums):
        res = [[]] * (1 << len(nums))
        # 把以上的嵌套循环该成两个并列循环
        for i in range(len(nums)):  # 填写基本case：每个位置分别为1
            res[1 << i] = [nums[i]]
        for mask in range(3, 1 << len(nums)):  # 0，1，2 属于基本case，已经填写过
            res[mask] = res[mask & -mask] + res[mask & mask - 1]
        return res


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

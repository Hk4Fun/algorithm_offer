__author__ = 'Hk4Fun'
__date__ = '2018/3/28 23:09'
'''题目描述：
You're given a matrix represented by a two-dimensional array, 
and two positive integers r and c representing the row number 
and column number of the wanted reshaped matrix, respectively.
The reshaped matrix need to be filled with all the elements 
of the original matrix in the same row-traversing order as they were.
If the 'reshape' operation with given parameters is possible and legal, 
output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4
Output: 
[[1,2,3,4]]
Explanation:
The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:
Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4
Output: 
[[1,2],
 [3,4]]
Explanation:
There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Note:
The height and width of the given matrix is in range [1, 100].
The given r and c are all positive.
'''


class Solution:
    """
    :type nums: List[List[int]]
    :type r: int
    :type c: int
    :rtype: List[List[int]]
    """

    def matrixReshape1(self, nums, r, c):
        if r == len(nums) or r * c != len(nums) * len(nums[0]):
            return nums
        res = [[]]
        for i in range(len(nums)):
            for j in range(len(nums[0])):
                k = nums[i][j]
                res[-1].append(k) if len(res[-1]) < c else res.append([k])
        return res

    def matrixReshape2(self, nums, r, c):
        if r == len(nums) or r * c != len(nums) * len(nums[0]):
            return nums
        res = [[0] * c for _ in range(r)]
        n = len(nums[0])
        for i in range(r * c):  # 一层循环搞定
            res[i // c][i % c] = nums[i // n][i % n]
        return res

    def matrixReshape3(self, nums, r, c):
        A = [x for row in nums for x in row]  # 多用一个临时数组来存储数值
        return [A[i * c:(i + 1) * c] for i in range(r)] if r * c == len(A) else nums  # 用分片


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

        matrix = [[1, 2], [3, 4]]
        testArgs.append([matrix, 1, 4, [[1, 2, 3, 4]]])

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

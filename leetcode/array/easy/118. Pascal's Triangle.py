__author__ = 'Hk4Fun'
__date__ = '2018/3/25 0:46'
'''题目描述：
Given numRows, generate the first numRows of Pascal's triangle.
For example, given numRows = 5,
Return
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''
'''主要思路：
思路1：按照规律依次生成下一行
思路2：每一行都可如下面所示生成（上一行分别首位补0相加）：
    1 3 3 1 0 
 +  0 1 3 3 1
 =  1 4 6 4 1
'''


class Solution:
    def generate1(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for row_num in range(numRows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle

    def generate2(self, numRows):  # pythonic，use map()
        res = [[1]]
        for _ in range(numRows - 1):
            res.append(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))
        return res

    def generate3(self, numRows):  # pythonic, use zip()
        res = [[1]]
        for _ in range(numRows - 1):
            res.append([x + y for x, y in zip([0] + res[-1], res[-1] + [0])])
        return res





# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 100000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        expected = [
            [1],
            [1, 1],
            [1, 2, 1],
            [1, 3, 3, 1],
            [1, 4, 6, 4, 1]
        ]
        testArgs.append([5, expected])

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

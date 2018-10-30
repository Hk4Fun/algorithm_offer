__author__ = 'Hk4Fun'
__date__ = '2018/8/9 8:53'
'''题目描述：
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
Note:

You have to rotate the image in-place, 
which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Given input matrix = 
[
  [1,2,3],
  [4,5,6],
  [7,8,9]
],

rotate the input matrix in-place such that it becomes:
[
  [7,4,1],
  [8,5,2],
  [9,6,3]
]
Example 2:

Given input matrix =
[
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
], 

rotate the input matrix in-place such that it becomes:
[
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]
'''
'''主要思路：
思路1：anti-clockwise(A) = T(A) -> A[::-1]    (T(A)表示矩阵的转置)
            clockwise(A) = A[::-1] -> T(A)  

思路2：
    anti-clockwise(A)：A[i][j], A[~j][i], A[~i][~j], A[j][~i]
                     =  A[j][~i], A[i][j], A[~j][i], A[~i][~j]
                     
         clockwise(A)：A[i][j], A[~j][i], A[~i][~j], A[j][~i] 
                     = A[~j][i], A[~i][~j], A[j][~i], A[i][j]
      注意：由于python切片的特性，A[~i] 等于 A[n-i-1]
       
思路3：pythonic，使用zip
       anti-clockwise(A) = list(zip(*A))[::-1]
            clockwise(A) = zip(*A[::-1])


'''


class Solution:
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """

    def rotate1(self, A):
        A.reverse()
        for i in range(len(A)):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]

    def rotate2(self, A):
        n = len(A)
        for i in range(n // 2):
            for j in range(n - n // 2):
                A[i][j], A[~j][i], A[~i][~j], A[j][~i] = \
                    A[~j][i], A[~i][~j], A[j][~i], A[i][j]

    def rotate3(self, A):  # 实际上不算是in-place
        A[:] = map(list, zip(*A[::-1]))


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

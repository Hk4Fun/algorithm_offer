__author__ = 'Hk4Fun'
__date__ = '2018/1/1 12:22'

'''题目描述：
在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''
'''主要思路：
从右上角或左下角开始查找，这里选择右上角
如果当前元素大于target, 剔除target所在列（col左移-1），
如果当前元素小于target, 剔除target所在行（row下移+1），
否则等于，结束查找。
每一次查找都在数组的查找范围中剔除一行或一列，每一步都缩小了查找的范围
直到找到要查找的数字，或者查找范围为空
'''


class Solution:
    def Find(self, array, target):
        if not target or not array:  # 鲁棒性
            return False
        rows, cols = len(array), len(array[0])
        row, col = 0, cols - 1
        while row < rows and col >= 0:
            if array[row][col] > target:  # 当前元素大于target, 剔除target所在列（col左移-1）
                col = col - 1
            elif array[row][col] < target:  # 当前元素小于target, 剔除target所在行（row下移+1）
                row = row + 1
            else:  # 等于，结束查找
                return True
        return False


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        array = [[1, 2, 8, 9],
                 [2, 4, 9, 12],
                 [4, 7, 10, 13],
                 [6, 8, 11, 15]]

        testArgs = []
        testArgs.append([array, 7, True])  # 要查找的数在数组中
        testArgs.append([array, 5, False])  # 要查找的数不在数组中
        testArgs.append([array, 1, True])  # 要查找的数是数组中最小的数字
        testArgs.append([array, 15, True])  # 要查找的数是数组中最大的数字
        testArgs.append([array, 0, False])  # 要查找的数比数组中最小的数字还小
        testArgs.append([array, 16, False])  # 要查找的数比数组中最小的数字还大
        testArgs.append(['', [], False])  # 鲁棒性测试，输入None

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

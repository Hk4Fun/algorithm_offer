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

import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def Test(testName, array, target, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.Find(array, target)
        end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return

    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


array = [[1, 2, 8, 9],
         [2, 4, 9, 12],
         [4, 7, 10, 13],
         [6, 8, 11, 15]]

Test('Test1', array, 7, True)  # 要查找的数在数组中
Test('Test2', array, 5, False)  # 要查找的数不在数组中
Test('Test3', array, 1, True)  # 要查找的数是数组中最小的数字
Test('Test4', array, 15, True)  # 要查找的数是数组中最大的数字
Test('Test5', array, 0, False)  # 要查找的数比数组中最小的数字还小
Test('Test6', array, 16, False)  # 要查找的数比数组中最小的数字还大
Test('Test7', '', [], False)  # 鲁棒性测试，输入None

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))

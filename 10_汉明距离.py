__author__ = 'Hk4Fun'
__date__ = '2018/1/4 15:14'

'''题目描述：
求两个整数的汉明距离（不相同的二进制位数）
'''
'''主要思路：
先异或再统计异或结果中1的个数
'''


class Solution:
    def HammingDistance(self, n, m):
        diff = m ^ n  # 异或后的结果对python来讲就是正数，即使首位为1（相当于无符号整数）
        count = 0
        while diff:
            count += 1
            diff = diff & (diff - 1)
        return count


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def Test(testName, n, m, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    try:
        start = timeit.default_timer()
        result = test.HammingDistance(n, m)
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


Test('Test1', 0b0101, 0b1010, 4)
Test('Test2', 0b0101, 0b0101, 0)
Test('Test3', 0b0000, 0b0000, 0)
Test('Test4', 0b1111, 0b1111, 0)
Test('Test5', 0b1111, 0b0000, 4)
Test('Test6', 0b1111, 0b1110, 1)
Test('Test7', 0b1111, 0b1100, 2)
Test('Test8', 0b1111, 0b1000, 3)

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))

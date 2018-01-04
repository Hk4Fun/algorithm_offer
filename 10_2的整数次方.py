__author__ = 'Hk4Fun'
__date__ = '2018/1/4 14:59'

'''题目描述：
判断一个整数是不是2的整数次方
'''
'''主要思路：
一个整数如果是2的整数次方，那么它的二进制表示中有且仅有一位是1，
而其他所有位都是0。那么根据上一题，只需把这个整数减去1后再和它自己做与运算，
这个整数中唯一的1就会变成0（注意这里2的整数次幂一定大于0）
'''


class Solution:
    def PowerOf2(self, n):
        return True if n > 0 and n & (n - 1) == 0 else False


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def Test(testName, n, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0
    try:
        start = timeit.default_timer()
        result = test.PowerOf2(n)
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


Test('Test1', 1, True)  # 2^0=1
Test('Test2', 2, True)
Test('Test3', 10, False)
Test('Test4', 32, True)
Test('Test5', 0, False)
Test('Test6', -1, False)


print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))

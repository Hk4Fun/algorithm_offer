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
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        testArgs.append([1, True])  # 2^0=1
        testArgs.append([2, True])
        testArgs.append([10, False])
        testArgs.append([32, True])
        testArgs.append([0, False])
        testArgs.append([-1, False])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

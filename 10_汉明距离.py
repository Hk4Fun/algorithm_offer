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
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        testArgs.append([0b0101, 0b1010, 4])
        testArgs.append([0b0101, 0b0101, 0])
        testArgs.append([0b0000, 0b0000, 0])
        testArgs.append([0b1111, 0b1111, 0])
        testArgs.append([0b1111, 0b0000, 4])
        testArgs.append([0b1111, 0b1110, 1])
        testArgs.append([0b1111, 0b1100, 2])
        testArgs.append([0b1111, 0b1000, 3])

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

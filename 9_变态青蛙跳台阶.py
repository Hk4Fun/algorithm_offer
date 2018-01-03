__author__ = 'Hk4Fun'
__date__ = '2018/1/4 2:46'

'''题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
'''主要思路：
由上一题可以推出：f(n) = f(n-1) + f(n-2) + f(n-3) + ...... + f(1) + f(0)，其中 f(0) = 1
求得通项公式为：f(n) = 2^(n-1)，其中 n >= 1，且 f(0) = 1
'''

class Solution:
    def jumpFloorII(self, n):
        f = 1
        for i in range(n-1):
            f *= 2
        return f
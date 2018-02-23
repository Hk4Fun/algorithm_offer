__author__ = 'Hk4Fun'
__date__ = '2018/1/4 2:34'

'''题目描述：
一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
'''主要思路：
n=1时，f(n)=1
n=2时，f(n)=2
当n>2时，跳法总数 = 跳1级后剩下的n-1级的跳法总数 + 跳2级后剩下的n-2级的跳法总数
即 f(n) = f(n-1) + f(n-2)，转换成斐波那契数列问题
'''


class Solution:
    def jumpFloor(self, n):
        tempArray = [1, 2]
        if n >= 3:
            for i in range(3, n + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]  # 注意这里 i%2 的巧妙
        return tempArray[(n + 1) % 2]

__author__ = 'Hk4Fun'
__date__ = '2018/1/4 3:14'

'''题目描述：
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？(n>=0)
'''
'''主要思路：
若第一个矩形竖着放，则右边剩下 2*(n-1);
若第一个矩形横着放，则下面必须也要横着放一个，此时右边剩下 2*(n-2)
所以还是一个斐波那契问题：f(n) = f(n-1) + f(n-2)，其中f(1)=1, f(2)=2
'''


class Solution:
    def rectCover(self, number):
        if number == 0:
            return 0
        tempArray = [1, 2]
        if number >= 3:
            for i in range(3, number + 1):
                tempArray[(i + 1) % 2] = tempArray[0] + tempArray[1]
        return tempArray[(number + 1) % 2]

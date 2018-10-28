__author__ = 'Hk4Fun'
__date__ = '2018/2/9 21:55'

'''题目描述：
输入一个整型数组，数组中一个或连续的多个整数组成一个子数组。
求所有子数组的和的最大值，要求时间复杂度为O(n)
'''
'''主要思路：
一个长度为n的数组，总共有n(n-1)/2个子数组：以第i个数为结尾的子数组有i个(1 <= i <= n)
先从一个例子入手：[a,b,c,d]:
以a为结尾的子数组和有1个,记为f(1)={a}
以b为结尾的子数组和有2个,记为f(2)={b,a+b}
以c为结尾的子数组和有3个,记为f(3)={c,b+c,a+b+c}
以d为结尾的子数组和有4个,记为f(4)={d,c+d,b+c+d,a+b+c+d)
从后往前看，设f(0)={}，则：
F(4) = max(f(4)) = max(d,f(3)+d) = max(d,F(3)+d)
F(3) = max(f(3)) = max(c,f(2)+c) = max(c,F(2)+c)
F(2) = max(f(2)) = max(d,f(1)+d) = max(d,F(1)+d)
F(1) = max(f(1)) = max(a,f(0)+a) = max(a,F(0)+a)
可以写出递归表达式：
       array[i]        ,i=0 or F(i-1)<=0
F(i)={
       F(i-1)+array[i] ,i!=0 and F(i-1)>0 
则max(F(i))为所有子数组的和的最大值
这个公式的意义是：当以第i-1个数字结尾的子数组中所有数字的和小于0时，
如果把这个负数与第i个数累加，得到的结果比第i个数字本身还要小，所以
这种情况下舍弃前面的累加而直接选择第i个数字本身作为最大值。当然，
若以第i-1个数字结尾的子数组中所有数字的和大于0，则选择累加作为最大值
基于以上的分析归纳，就有了两种实现方式：递归和循环，二者异曲同工
但循环实现是最佳的，因为避免了重复计算和堆栈调用，时间空间都最佳

更新：以上思路其实是一种动态规划的思想：
设f(i)为以第i个数结尾的连续子数组的最大和，则状态转移方程为：
f(i) = max(f(i-1)+array[i], array[i])
最后结果为max(f(i))
优化：f(i)只与f(i-1)有关，即只与前一状态有关，所以空间上可以由O(n)降为O(1)

暴力解法时间O(n^2),空间O(1)，而优化后的动态规划时间O(n),空间O(1)
'''


class Solution:
    # 递归实现
    def FindGreatestSumOfSubArray1(self, array):
        if not array:
            return

        def F(i):
            if i == 0 or F(i - 1) <= 0:
                return array[i]
            else:
                return F(i - 1) + array[i]

        return max(F(i) for i in range(len(array)))

    # 循环实现，是递归的改进，用一个数组存放各个最大和，避免重复计算
    def FindGreatestSumOfSubArray2(self, array):
        if not array:
            return
        MaxSum = []
        for i in range(len(array)):
            if i == 0 or MaxSum[i - 1] <= 0:
                MaxSum.append(array[i])
            else:
                MaxSum.append(MaxSum[i - 1] + array[i])
        return max(MaxSum)

    # 循环实现，是上一方法的改进，不必用MaxSum来存放，
    # 直接GreatestSum存放最大和即可，在循环中更新最大和
    def FindGreatestSumOfSubArray3(self, array):
        if not array:
            return

        CurSum = 0  # 相当于递归中的F(i)，即动态规划中的备忘录（已优化）
        GreatestSum = array[0]  # 相当于递归中的max(F(i))
        for i in range(len(array)):
            if CurSum <= 0:  # 当前累加和小于0，则没有必要接着累加
                CurSum = array[i]
            else:  # 否则继续累加
                CurSum += array[i]

            if CurSum > GreatestSum:  # 更新最大和
                GreatestSum = CurSum

        return GreatestSum

    def FindGreatestSumOfSubArray4(self, array):
        # 简化版
        if not array: return
        curSum = maxSum = array[0]
        for num in array[1:]:
            curSum = max(num, curSum + num)
            maxSum = max(maxSum, curSum)
        return maxSum


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([[1, -2, 3, 10, -4, 7, 2, -5], 18])

        # 所有数字都是负数
        testArgs.append([[-2, -8, -1, -5, -9], -1])

        # 所有数字都是正数
        testArgs.append([[2, 8, 1, 5, 9], 25])

        # 只有一个数字
        testArgs.append([[0], 0])

        # 空数组
        testArgs.append([[], None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

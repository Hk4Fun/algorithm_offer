__author__ = 'Hk4Fun'
__date__ = '2018/2/10 21:06'

'''题目描述：
把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。
习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。
'''
'''主要思路：
思路1：逐个判断每个数是否为丑数，直观但不够高效。
       如果一个数能被2整除，就把它连续除以2；
       如果能被3整除，就把它连续除以3；
       如果能被5整除，就把它连续除以5。
       如果最后我们得到的是1，那么这个数就是丑数。
       该算法最大的问题就是每个整数都要计算，
       即使一个数字不是丑数我们还是要对它进行求余和除法操作。
思路2：创建数组保存已经找到的丑数并排好序，关键在于如何生成下一个丑数
       数组中最后一个丑数最大，记为M。设置index2，标记该位置的数乘以2大于M，
       同理设置index3、index5，这样每次只需求min(A[index2]*2,A[index3]*3,A[index5]*5)
       就可求出下一个丑数，然后更新三个标记。这样关键就在于如何更新这三个标记，
       对于index2，只需往后遍历，直到指向的那个数乘2大于M即可停止，其他两个同理。
       空间换时间，比思路1时间上快了不少
思路3：对思路2的改进，对于如何更新那三个标记，仔细推敲可以发现其实
       只需让那些指向的数乘相应因子等于当前M的标记往后移一位即可，
       因为 M = min(A[index2]*2,A[index3]*3,A[index5]*5)，则至少有个标记是要往后移的，
       且移一位即可，后面那个数乘以相应的因子一定大于M。
       那么其他指向的数乘相应因子不等于当前M的标记为什么没有必要移动呢？
       还是因为 M = min(A[index2]*2,A[index3]*3,A[index5]*5)， 既然M是其中最小的，
       那么其他的标记所指向的数乘以相应因子一定就比M大了，没有必要更新
       这样就可以把思路2中的三个并列的while简化成三个并列的if
       
更新：这里谈谈为什么要使用这三个index，且为什么这样做可以保证按顺序产生下一个丑数。
按照正常的理解，后面的丑数都是由前面已经产生的某个丑数乘2或乘3或乘5得到，为了按照顺序，
必须把前面每个丑数乘2或乘3或乘5得到的值中取大于当前最后一个丑数的最小值。
那么问题来了，有必要把每个丑数都乘这三个因子然后取最小值？
我们发现每个丑数都要经历乘2乘3乘5的过程，但却没有必要在同一次竞争下一个丑数中乘，
所以我们反过来，标记上那些需要乘2或乘3或乘5的数，使得index2指向的数就要乘2，
因为它在下一次竞争中可能会胜利，index3和index5同理。为了满足以上规则，
我们让这三个标记从左向右各自独立遍历，这样也就让每个数都会经历乘2或乘3或乘5的过程，
且如果标记的数乘以相应因子后竞争胜利了，那么该标记就要往后挪1位，
因为新的丑数是该标记因子乘以它指向的数竞争胜利而生成的，
所以该数乘以该因子已经没有参与下一次竞争的机会了，相应的因子标记就该往后挪，
使得下一个数参与新的竞争。而其他竞争失败的标记不用动，因为它们还有竞争胜利的机会，
毕竟每次胜利的是那个乘积最小的。
'''


class Solution:
    def GetUglyNumber1(self, index):
        def isUgly(number):
            while number % 2 == 0:
                number //= 2
            while number % 3 == 0:
                number //= 3
            while number % 5 == 0:
                number //= 5
            return number == 1

        if not index or index <= 0:
            return 0
        number = uglyFound = 0
        while uglyFound < index:
            number += 1
            if isUgly(number):
                uglyFound += 1
        return number

    def GetUglyNumber2(self, index):
        if not index or index <= 0:
            return 0
        uglyNumbers = [1]
        index2 = index3 = index5 = 0
        for i in range(1, index):
            # 竞争产生下一个丑数
            uglyNumbers.append(min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5))
            while uglyNumbers[index2] * 2 <= uglyNumbers[-1]: index2 += 1
            while uglyNumbers[index3] * 3 <= uglyNumbers[-1]: index3 += 1
            while uglyNumbers[index5] * 5 <= uglyNumbers[-1]: index5 += 1
        return uglyNumbers[-1]

    def GetUglyNumber3(self, index):
        if not index or index <= 0:
            return 0
        if index < 7:  # 小于7的丑数连续
            return index
        uglyNumbers = [1]
        index2 = index3 = index5 = 0
        for i in range(1, index):
            # 竞争产生下一个丑数
            uglyNumbers.append(min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5))
            # 把思路2中的三个并列的while简化成三个并列的if
            # 则三个if只有一个会执行，也就是说只有一个标记会往后移，就是那个在上面竞争胜利的那个标记
            # 胜利的标记后移，而其他两个失败的标记原地不动，因为它俩还有胜利的机会
            if uglyNumbers[-1] == uglyNumbers[index2] * 2: index2 += 1
            if uglyNumbers[-1] == uglyNumbers[index3] * 3: index3 += 1
            if uglyNumbers[-1] == uglyNumbers[index5] * 5: index5 += 1
        return uglyNumbers[-1]


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        self.debug = False
        testArgs = []

        testArgs.append([1, 1])
        testArgs.append([2, 2])
        testArgs.append([3, 3])
        testArgs.append([4, 4])
        testArgs.append([5, 5])
        testArgs.append([6, 6])
        testArgs.append([7, 8])
        testArgs.append([8, 9])
        testArgs.append([9, 10])
        testArgs.append([10, 12])
        testArgs.append([11, 15])
        # testArgs.append([1500, 859963392])
        testArgs.append([0, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

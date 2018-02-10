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
思路3：对思路2的改进，对于如何更新那三个标记，仔细推敲可以发现其实
       只需让那些指向的数乘相应因子等于当前M的标记往后移一位即可，
       因为 M = min(A[index2]*2,A[index3]*3,A[index5]*5)，则至少有个标记是要往后移的，
       且移一位即可，后面那个数乘以相应的因子一定大于M。
       那么其他指向的数乘相应因子不等于当前M的标记为什么没有必要移动呢？
       还是因为 M = min(A[index2]*2,A[index3]*3,A[index5]*5)， 既然M是其中最小的，
       那么其他的标记所指向的数乘以相应因子一定就比M大了，没有必要更新
       这样就可以把思路2中的三个并列的while简化成三个并列的if
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
            uglyNumbers.append(min(uglyNumbers[index2] * 2, uglyNumbers[index3] * 3, uglyNumbers[index5] * 5))
            # 把思路2中的三个并列的while简化成三个并列的if
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
        testArgs.append([1500, 859963392])
        testArgs.append([0, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

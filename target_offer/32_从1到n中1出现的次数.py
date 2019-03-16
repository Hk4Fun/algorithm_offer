__author__ = 'Hk4Fun'
__date__ = '2018/2/10 1:05'

'''题目描述：
原题：输入一个整数n，求从1到n这n个整数的十进制表示中1出现的次数
扩展：改成X出现的次数，X∈[1,9]
'''
'''主要思路：
链接：https://www.nowcoder.net/questionTerminal/bd7f978302044eee894445e244c7eee6
来源：牛客网
参考博文：http://www.cnblogs.com/nailperry/p/4752987.html，主要就是从数字出发找规律。
一、1的数目
编程之美上给出的规律：
1. 如果第i位（自右至左，从1开始标号）上的数字为0，则第i位可能出现1的次数由更高位决定
  （若没有高位，视高位为0），等于更高位数字*当前位数的权重10^(i-1)。
2. 如果第i位上的数字为1，则第i位上可能出现1的次数不仅受更高位影响，还受低位影响
  （若没有低位，视低位为0），等于更高位数字*当前位数的权重10^(i-1)+（低位数字+1）。
3. 如果第i位上的数字大于1，则第i位上可能出现1的次数仅由更高位决定（若没有高位，视高位为0），
   等于（更高位数字+1）*当前位数的权重10^(i-1)。
二、X的数目
这里的X∈[1,9]，因为X=0不符合下列规律，需要单独计算。
首先要知道以下的规律：
从 1 至 10，在它们的个位数中，任意的 X 都出现了 1 次。
从 1 至 100，在它们的十位数中，任意的 X 都出现了 10 次。
从 1 至 1000，在它们的百位数中，任意的 X 都出现了 100 次。
依此类推，从1至10^i，在它们的左数第二位（右数第i位）中，任意的X都出现了10^(i-1)次。
这个规律很容易验证，这里不再多做说明。
接下来以 n=2593,X=5 为例来解释如何得到数学公式。从 1 至 2593 中，数字 5 总计出现了 813 次，
其中有 259 次出现在个位，260 次出现在十位，294 次出现在百位，0 次出现在千位。
现在依次分析这些数据，首先是个位。从 1 至 2590 中，包含了 259 个 10，因此任意的 X 都出现了 259 次。
最后剩余的三个数 2591, 2592 和 2593，因为它们最大的个位数字 3 < X，因此不会包含任何 5。
（也可以这么看，3<X，则个位上可能出现的X的次数仅由更高位决定，等于更高位数字（259）X10^(1-1)=259）。
然后是十位。从 1 至 2500 中，包含了 25 个 100，因此任意的 X 都出现了  25×10=250  次。
剩下的数字是从 2501 至 2593，它们最大的十位数字 9 > X，因此会包含全部 10 个 5。
最后总计 250 + 10 = 260。（也可以这么看，9>X，则十位上可能出现的X的次数仅由更高位决定，
等于更高位数字（25+1）X10^(2-1)=260）。
接下来是百位。从 1 至 2000 中，包含了 2 个 1000，因此任意的 X 都出现了  2×100=200  次。
剩下的数字是从 2001 至 2593，它们最大的百位数字 5 == X，这时情况就略微复杂，
它们的百位肯定是包含 5 的，但不会包含全部 100 个。如果把百位是 5 的数字列出来，
是从 2500 至 2593，数字的个数与百位和十位数字相关，是 93+1 = 94。最后总计 200 + 94 = 294。
（也可以这么看，5==X，则百位上可能出现X的次数不仅受更高位影响，还受低位影响，
等于更高位数字（2）X10^(3-1)+（93+1）=294）。
最后是千位。现在已经没有更高位，因此直接看最大的千位数字 2 < X，所以不会包含任何 5。
（也可以这么看，2<X，则千位上可能出现的X的次数仅由更高位决定，等于更高位数字（0）X10^(4-1)=0）。
到此为止，已经计算出全部数字 5 的出现次数。
总结一下以上的算法，可以看到，当计算右数第 i 位包含的 X 的个数时：
取第i位左边（所有高位）的数字，乘以  10^(i-1) ，得到基础值  a 。
取第i位数字，计算修正值：
如果小于 X，则结果为  a 。
如果大于 X，则结果为  a+ 10^(i-1) 。
如果等于 X，则取第 i 位右边（所有低位）数字，设为  b ，最后结果为  a+b+1 。
相应的代码非常简单，效率也非常高，时间复杂度只有  O( log n) 。
'''


class Solution:
    def NumberOfxBetween1AndN_1(self, n, x):
        if n < 0 or x < 1 or x > 9:  # 检查n和x的范围
            return 0
        count, weight = 0, 1  # 从右至左，计算每一位出现的次数（为了简化计算，不用i表示第i位，而用权重表示，异曲同工）
        while weight <= n:
            high = n // weight  # 第i位的高位，包含第i位
            low = n % weight  # 第i位的低位
            cur = high % 10  # 第i位本身
            base = (high // 10) * weight  # 计算基础值，high//10就不含第i位了
            if cur < x:  # 第i位小于x
                count += base
            elif cur > x:  # 第i位大于x
                count += base + weight
            else:  # 第i位等于x
                count += base + low + 1
            weight *= 10  # 左移一位，权值*10
        return count

    # 下面这个是对上面的简化， 将三种情况统一到一个表达式中
    def NumberOfxBetween1AndN_2(self, n, x):
        if n < 0 or x < 1 or x > 9:
            return 0
        count, weight = 0, 1
        while weight <= n:
            # 9-x补上一个差值，把大于x和小于等于x是否加上weight给统一了，
            # 若x=1，则补上8，注意到 n // weight 是包含第i位本身的，
            # 那么当第i位大于x，即大于1时，加上8后产生进位，使得多加一个weight
            # x的其他情况类似。
            # 而(n // weight % 10 == x)把小于等于x时是否加上low + 1给统一了
            count += (n // weight + 9 - x) // 10 * weight + (n // weight % 10 == x) * (n % weight + 1)
            weight *= 10
        return count

    # 下面这个是最原始的算法，不推荐。从1遍历到n，对每个数都一一取出各个位来检查是否为x
    # def NumberOfxBetween1AndN_3(self, n, x):
    #     if n < 0 or x < 1 or x > 9:
    #         return 0
    #     count = 0
    #     for i in range(1, n + 1):
    #         while i:
    #             if i % 10 == x:
    #                 count += 1
    #             i //= 10
    #     return count


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([1, 1, 1])
        testArgs.append([5, 1, 1])
        testArgs.append([10, 1, 2])
        testArgs.append([55, 1, 16])
        testArgs.append([99, 1, 20])
        testArgs.append([10000, 1, 4001])
        testArgs.append([21345, 1, 18821])

        testArgs.append([1, 2, 0])
        testArgs.append([5, 2, 1])
        testArgs.append([12, 2, 2])
        testArgs.append([55, 2, 16])
        testArgs.append([99, 2, 20])
        testArgs.append([10000, 2, 4000])
        testArgs.append([21345, 2, 9821])

        testArgs.append([2593, 5, 813])

        testArgs.append([0, 1, 0])
        testArgs.append([0, 2, 0])
        testArgs.append([-1, 10, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

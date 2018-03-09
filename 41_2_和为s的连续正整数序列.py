__author__ = 'Hk4Fun'
__date__ = '2018/2/15 0:45'

'''题目描述：
找出所有和为S的连续正整数序列(至少含有两个数)。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
'''
'''主要思路：
思路1：用两个数small和big分别表示序列的最小值和最大值。首先把small初始化为1，big初始化为2。
       如果从small到big的序列的和大于s，可以从序列中去掉较小值，也就是增大small的值。
       如果从small到big的序列的和小于s，可以增大big，让序列包含更多的数字。
       因为序列至少要有两个连续的数字，所以small的上限是(s-1)/2，big的上限是(s-1)/2+1
思路2：双指针问题，当总和小于sum，大指针继续+，否则小指针+。实际上和思路1没什么区别，只是代码结构清晰一些。
       但由于没有上限，使得情况发生重复，所以时间效率反而没有思路1好
思路3：根据数学公式推导：(a1+an)*n/2=s, n=an-a1+1  ==>  (an+a1)*(an-a1+1)=2s=i*j(设i>=j), 其中i=an+a1, j=an-a1+1
       由 i=an+a1, j=an-a1+1 解得 an=(i+j-1)/2, a1=(i-j+1)/2 。所以只需遍历i和j，但i和j有条件，因为an和a1为正整数，
       所以(i+j)和(i-j)必须为奇数，也就是说i和j必为一奇一偶，所以i>j。所以j的上限为sqrt(2s)，而j的下限为2，若为1则i=2s，
       an=a1=s，不合题意。那么如何判断i和j是否一奇一偶呢？(i^j)&1==1时i和j必为一奇一偶
思路4：1）由于我们要找的是和为S的连续正整数序列，因此这个序列是个公差为1的等差数列，所以这个序列的中间值代表了平均值的大小。
          假设序列长度为n，那么这个序列的中间值可以通过（S / n）得到，知道序列的中间值和长度，也就不难求出这段序列了。
          所以只需遍历n的值即可。
       2）满足条件的n分两种情况：
          n为奇数时，序列中间的数正好是序列的平均值，所以条件为：
          (n & 1) == 1 && sum % n == 0；
          n为偶数时，序列中间两个数的平均值是序列的平均值，而这个平均值的小数部分为0.5，所以条件为：
          (n & 1) == 0 && (sum % n) * 2 == n.
       3）由题可知n >= 2，那么n的最大值是多少呢？我们让序列从1开始，根据等差数列的求和公式：S = (1 + n) * n / 2，
          得到 n <= sqrt(2s).
'''


class Solution:
    def FindContinuousSequence1(self, sum):
        if sum < 3:
            return []
        small = 1
        big = 2
        curSum = 3
        small_top = (sum - 1) >> 1
        big_top = small_top + 1
        result = []
        while small <= small_top and big <= big_top:
            while curSum > sum and small <= small_top:
                curSum -= small
                small += 1  # 先减再右移
            if curSum == sum:
                result.append(list(range(small, big + 1)))
            big += 1  # 如果curSum < sum，那么big后移；如果找到了一个序列，那么big也后移继续寻找下一个序列
            curSum += big  # 先右移再加
        return result

    def FindContinuousSequence2(self, sum):
        if sum < 3:
            return []
        small = 1
        big = 2
        result = []
        while big > small:
            curSum = (small + big) * (big - small + 1) >> 1
            if curSum < sum:
                big += 1
            elif curSum > sum:
                small += 1
            else:
                result.append(list(range(small, big + 1)))
                big += 1  # 在这里small+=1也可以，思路1是因为把两种情况合在一起才只能是big += 1
        return result

        # def FindContinuousSequence3(self, sum):

    def FindContinuousSequence3(self, sum):
        from math import sqrt
        if sum < 3:
            return []
        result = []
        # 之所以j取值从上限到下限反过来是因为题目要求序列间按照开始数字从小到大的顺序输出，
        # 也就是要求a1从小到大遍历。由a1 = (i - j + 1) / 2 和 i*j = 2s 可知，
        # 当j从大到小开始取值能保证(i - j)由小到大(i>j)，也就保证了a1由小到大
        for j in range(int(sqrt(sum << 1)), 1, -1):
            if 2 * sum % j == 0:
                i = 2 * sum // j
                if (i ^ j) & 1:
                    a1 = (i - j + 1) >> 1
                    an = (i + j - 1) >> 1
                    result.append(list(range(a1, an + 1)))
        return result

    def FindContinuousSequence4(self, sum):
        from math import sqrt
        if sum < 3:
            return []
        result = []
        # 同思路3，当n从由大至小遍历时，可以保证序列间按照开始数字从小到大的顺序
        for n in range(int(sqrt(sum << 1)), 1, -1):
            if (n & 1 == 1 and sum % n == 0) or (n & 1 == 0 and ((sum % n) << 1) == n):
                first = (sum // n) - ((n - 1) >> 1)
                result.append(list(range(first, first + n)))
        return result


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([1, []])

        testArgs.append([3, [[1, 2]]])

        testArgs.append([4, []])

        testArgs.append([9, [[2, 3, 4], [4, 5]]])

        testArgs.append([15, [[1, 2, 3, 4, 5], [4, 5, 6], [7, 8]]])

        testArgs.append([100, [[9, 10, 11, 12, 13, 14, 15, 16], [18, 19, 20, 21, 22]]])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

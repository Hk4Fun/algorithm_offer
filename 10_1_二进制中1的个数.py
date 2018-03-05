__author__ = 'Hk4Fun'
__date__ = '2018/1/4 3:20'

'''题目描述：
输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''
'''主要思路：
思路1：每次右移一位并和1相与，为1则说明该位为1，
       但如果是负数则右移时左边补1，所以可以控制循环次数为32
思路2：在思路1的基础上，既然负数右移时最高位补1，
       那我们可以把负数&0x7fffffff，这样就把负数转成正数，
       唯一差别就是最高位1变成0，少了一个1，所以count+1，
       之后按照正数处理即可，这样就可以不用控制循环次数了（n为0时退出）
思路3：前面的思路都是让n右移，不如换个思维，让1左移然后与n相与
       由于python中整数无限大，所以要控制循环次数32，
       而c/c++/java中1在int左移32次下自动为0，不用控制次数
思路4：利用一个位运算技巧：一个整数减1后总是把它的最右边的1变为0
       这里有两种情况：最右边的1在最末位和不在最末位
       但无论怎样，减一后的数与原数相与就一定可以把最右的1变为0
       但有一点要注意：由于c/c++/java中int位数限定32位，
       所以n最后一定被全部变为0，循环退出；但python就有区别了，
       python的整数位数不止32位，所以在负数情况下1的位数会多出很多，
       所以应先&0xffffffff，保留后面32位，前面全部变成0
思路5：平行算法，有点类似于二分，
       原理：若相邻的两个bit为00则相加为00， 相邻的两个bit为01或10则相加为01，
       相邻两个数为11则相加为10，即相邻位相加，结果就是它们的1的个数，重复这个过程，
       直到只剩下一位。例如0x11530828的二进制1个数统计过程如下：
        0001 0001 1001 0011 0000 1000 0010 1000
        0 1  0 1  1 1  0 2  0 0  1 0  0 1  1 0
        1    1    2    2    0    1    1    1
        2         4         1         2 
        6                   3
        9
思路6：MIT HAKMEM算法：http://blog.csdn.net/msquare/article/details/4536388
       其中涉及到一个求模运算，可能会减慢速度，可以用其他运算替代，
       C = A % B 等价于 C = A – B * (A / B)
       （考虑到负数的情况不能用&63替代%63）
思路7：先&0xffffffff保留后32位，再使用python内置方法 bin(n)，
       将n转成2进制字符串，然后再用 count('1') 统计字符1的个数
       （&0xffffffff也可以2**32+n替代）
'''


class Solution:
    def NumberOf1InBinary1(self, n):  # pythonic
        return sum([(n >> i) & 1 for i in range(32)])

    def NumberOf1InBinary2(self, n):
        count = 0
        if n < 0:
            n &= 0x7fffffff  # 转换成整数
            count += 1
        while n:  # 不必控制循环次数
            count += n & 1
            n >>= 1
        return count

    def NumberOf1InBinary3(self, n):  # pythonic
        return sum([(n & (1 << i)) >> i for i in range(32)])  # ">> i" 记得把结果移到最右边成为1

    def NumberOf1InBinary4(self, n):
        count = 0
        if n < 0:
            n &= 0xffffffff  # 去掉前面的1
        while n:  # 不必控制循环次数
            count += 1
            n &= (n - 1)
        return count

    def NumberOf1InBinary5(self, n):
        n = (n & 0x55555555) + ((n >> 1) & 0x55555555)
        n = (n & 0x33333333) + ((n >> 2) & 0x33333333)
        n = (n & 0x0f0f0f0f) + ((n >> 4) & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + ((n >> 8) & 0x00ff00ff)
        return (n & 0x0000ffff) + ((n >> 16) & 0x0000ffff)

    def NumberOf1InBinary6(self, n):
        tmp = n - ((n >> 1) & 0o33333333333) - ((n >> 2) & 0o11111111111)
        return ((tmp + (tmp >> 3)) & 0o30707070707) % 63

    def NumberOf1InBinary7(self, n):  # pythonic
        return bin(n).count('1') if n > 0 else bin(n & 0xffffffff).count('1')


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []

        # 注意：0xFFFFFFFF在python中不是负数了（相当于无符号整数），所以对于判断负数的算法只能直接传-1
        testArgs.append([0, 0])  # 0
        testArgs.append([1, 1])  # 正数
        testArgs.append([10, 2])  # 正数
        testArgs.append([-1, 32])  # 负数
        testArgs.append([-2, 31])  # 负数

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

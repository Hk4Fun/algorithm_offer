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
思路5：先&0xffffffff保留后32位，再使用python内置方法 bin(n)，
       将n转成2进制字符串，然后再用 count('1') 统计字符1的个数
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

    def NumberOf1InBinary5(self, n):  # pythonic
        return bin(n).count('1') if n > 0 else bin(n & 0xffffffff).count('1')


# ================================测试代码================================
import traceback
import timeit

pass_num = 0  # 通过测试的数量
test_num = 0  # 中的测试数量
time_pool = []  # 耗时


def Test(testName, method_type, n, expected):
    global pass_num, test_num
    if testName is not None:
        print('{} begins:'.format(testName))
    test_num += 1
    test = Solution()
    result = None
    start = end = 0
    try:
        if method_type == 1:
            start = timeit.default_timer()
            result = test.NumberOf1InBinary1(n)
            end = timeit.default_timer()
        elif method_type == 2:
            start = timeit.default_timer()
            result = test.NumberOf1InBinary2(n)
            end = timeit.default_timer()
        elif method_type == 3:
            start = timeit.default_timer()
            result = test.NumberOf1InBinary3(n)
            end = timeit.default_timer()
        elif method_type == 4:
            start = timeit.default_timer()
            result = test.NumberOf1InBinary4(n)
            end = timeit.default_timer()
        elif method_type == 5:
            start = timeit.default_timer()
            result = test.NumberOf1InBinary5(n)
            end = timeit.default_timer()
    except Exception as e:
        print('Failed:语法错误！')
        print(traceback.format_exc())
        return
    if (result == expected):
        print('Passed.\n')
        pass_num += 1
        time_pool.append(end - start)
    else:
        print('Failed:测试不通过！\n')


# 注意：0xFFFFFFFF在python中不是负数了（相当于无符号整数），所以对于判断负数的算法只能直接传-1
Test('Test1_1', 1, 0, 0)  # 0
Test('Test1_2', 1, 1, 1)  # 正数
Test('Test1_3', 1, 10, 2)  # 正数
Test('Test1_4', 1, -1, 32)  # 负数
Test('Test1_5', 1, -2, 31)  # 负数

# Test('Test2_1', 2, 0, 0)  # 0
# Test('Test2_2', 2, 1, 1)  # 正数
# Test('Test2_3', 2, 10, 2)  # 正数
# Test('Test2_4', 2, -1, 32)  # 负数
# Test('Test2_5', 2, -2, 31)  # 负数
#
# Test('Test3_1', 3, 0, 0)  # 0
# Test('Test3_2', 3, 1, 1)  # 正数
# Test('Test3_3', 3, 10, 2)  # 正数
# Test('Test3_4', 3, -1, 32)  # 负数
# Test('Test3_5', 3, -2, 31)  # 负数
#
# Test('Test4_1', 4, 0, 0)  # 0
# Test('Test4_2', 4, 1, 1)  # 正数
# Test('Test4_3', 4, 10, 2)  # 正数
# Test('Test4_4', 4, -1, 32)  # 负数
# Test('Test4_5', 4, -2, 31)  # 负数
#
# Test('Test5_1', 5, 0, 0)  # 0
# Test('Test5_2', 5, 1, 1)  # 正数
# Test('Test5_3', 5, 10, 2)  # 正数
# Test('Test5_4', 5, -1, 32)  # 负数
# Test('Test5_5', 5, -2, 31)  # 负数

print('测试结果：{}/{},{:.2f}%'.format(pass_num, test_num, (pass_num / test_num) * 100))
if pass_num:
    print('平均耗时：{:.2f}μs'.format((sum(time_pool) / pass_num) * 1000000))

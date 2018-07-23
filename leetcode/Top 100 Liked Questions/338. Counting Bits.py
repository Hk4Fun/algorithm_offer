__author__ = 'Hk4Fun'
__date__ = '2018/7/23 9:04'
'''题目描述：
Given a non negative integer number num. 
For every numbers i in the range 0 ≤ i ≤ num 
calculate the number of 1's in their binary representation and return them as an array.

Example:
For num = 5 you should return [0,1,1,2,1,2].

Follow up:

It is very easy to come up with a solution with run time O(n*sizeof(integer)). 
But can you do it in linear time O(n) /possibly in a single pass?
Space complexity should be O(n).
Can you do it like a boss? 
Do it without using any builtin function like __builtin_popcount in c++ or in any other language.
'''
'''主要思路：
先举几个例子找规律：
0-0000-0
--------
1-0001-1
--------
2-0010-1
3-0011-2
--------
4-0100-1
5-0101-2
6-0110-2
7-0111-3

思路1：时间O（n），空间O（n）
如果每次循环都去统计i中1的个数则会重复统计，因此可以先把i最右边的1去掉，
然后由数组下标映射得到已经统计过的数，其结果+1即可
思路2：时间O（n），空间O（n）
由思路1发现用到了备忘录的思想，因此想到可以用dp，其转移方程如下：
dp[i] = dp[i - offset] + 1
其中offset表示离i最近的2的幂数，如6离4最近，其offset为2，9里8最近，其offset为1
关键是如何在每次循环都可以直接得到offset，注意到offset等于保留i的最高位的1所得到的数
可以利用循环本身累计offset
思路3：时间O（n），空间O（n）
模仿思路1，去掉最右边的二进制位（右移即可），此时得到的数一定已经统计过，
可以直接通过下标映射，然后看被右移的那个二进制位是否为1，是的话其结果再加1即可
'''


class Solution:
    """
    :type num: int
    :rtype: List[int]
    """

    def countBits1(self, num):
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i & (i - 1)] + 1)
        return res

    def countBits2(self, num):
        res = [0]
        offset = 1
        for i in range(1, num + 1):
            if 2 * offset == i: offset *= 2
            res.append(res[i - offset] + 1)
        return res

    def countBits3(self, num):
        res = [0]
        for i in range(1, num + 1):
            res.append(res[i >> 1] + (i & 1)) # 注意这里(i & 1)要加上括号
        return res

# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])
        testArgs.append([])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

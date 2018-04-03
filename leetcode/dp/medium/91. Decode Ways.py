__author__ = 'Hk4Fun'
__date__ = '2018/4/3 14:54'
'''题目描述：
A message containing letters from A-Z is being encoded to numbers using the following mapping:
'A' -> 1
'B' -> 2
...
'Z' -> 26
Given an encoded message containing digits, determine the total number of ways to decode it.

For example,
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
The number of ways decoding "12" is 2.
'''
'''主要思路：
时间O（n），空间O（1）
dp[i]表示以s[i]结尾的字符串解码数, dp[i]初始化为0
若'1' <= s[i] <= '9'，则dp[i] += dp[i-1] 
若还有'10' <= s[i - 1:i + 1] <= '26'， 则dp[i] += dp[i-2]
由于只跟dp[i-1]和dp[i-2]有关，所以空间可以优化成O（1）
'''


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        prepre = 1
        pre = 1 if s[0] != '0' else 0
        for i in range(1, len(s)):
            cur = 0
            if '1' <= s[i] <= '9': cur += pre
            if '10' <= s[i - 1:i + 1] <= '26': cur += prepre
            prepre = pre
            pre = cur
        return pre


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
    solution = Solution()
    MyTest(solution=solution).start_test()

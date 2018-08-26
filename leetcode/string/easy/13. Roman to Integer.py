__author__ = 'Hk4Fun'
__date__ = '2018/8/26 15:50'
'''题目描述：
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, two is written as II in Roman numeral, just two one's added together. 
Twelve is written as, XII, which is simply X + II. 
The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII.
Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, 
which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. 
Input is guaranteed to be within the range from 1 to 3999.

Example 1:

Input: "III"
Output: 3
Example 2:

Input: "IV"
Output: 4
Example 3:

Input: "IX"
Output: 9
Example 4:

Input: "LVIII"
Output: 58
Explanation: C = 100, L = 50, XXX = 30 and III = 3.
Example 5:

Input: "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
'''
'''主要思路：
时间O（n），空间O（1）
'''


class Solution:
    """
    :type s: str
    :rtype: int
    """

    def romanToInt1(self, s):
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = i = 0
        sub = {'IV', 'IX', 'XL', 'XC', 'CD', 'CM'}
        while i < len(s):  # 从左到右扫描,自己控制下标
            if s[i:i + 2] in sub:
                sum += map[s[i + 1]] - map[s[i]]
                i += 2
            else:
                sum += map[s[i]]
                i += 1
        return sum

    def romanToInt2(self, s):
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = pre = 0
        for ch in s[::-1]:  # 从右到左扫描
            cur = map[ch]
            if cur >= pre:
                sum += cur
            elif cur < pre:
                sum -= cur
            pre = cur
        return sum

    def romanToInt3(self, s):
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        sum = pre = 0
        for ch in s:  # # 从左到右扫描
            cur = map[ch]
            if cur <= pre:
                sum += cur
            elif cur > pre:
                sum += cur - 2 * pre  # 减去前面加的，恢复原来的值，再减去一次得到正确的值
            pre = cur
        return sum


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1000  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append(["III", 3])
        testArgs.append(["IV", 4])
        testArgs.append(["IX", 9])
        testArgs.append(["LVIII", 58])
        testArgs.append(["MCMXCIV", 1994])

        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

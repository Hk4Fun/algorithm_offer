__author__ = 'Hk4Fun'
__date__ = '2018/4/1 12:52'
'''题目描述：
We have two special characters. The first character can be represented by one bit 0. 
The second character can be represented by two bits (10 or 11).

Now given a string represented by several bits. 
Return whether the last character must be a one-bit character or not. 
The given string will always end with a zero.

Example 1:
Input: 
bits = [1, 0, 0]
Output: True
Explanation: 
The only way to decode it is two-bit character and one-bit character. So the last character is one-bit character.

Example 2:
Input: 
bits = [1, 1, 1, 0]
Output: False
Explanation: 
The only way to decode it is two-bit character and two-bit character. So the last character is NOT one-bit character.

Note:
1 <= len(bits) <= 1000.
bits[i] is always 0 or 1.
'''
'''主要思路：
思路1（时间O（N），空间O（1））：
下标i从左到右扫描，遇到0，则i+1，表示匹配‘0’；遇到1，则i+2，表示匹配‘10’或‘01’。
由于最后一个一定为0，所以最终如果i来到最后一位，则表示匹配成功，否则i会超过最后一位，False

思路2（时间O（N），空间O（1））：
逆向思维，从后往前匹配，但是注意观察：不管是‘0’还‘10’，‘0’总是某个字符的结尾
所以如果存在倒数第二个0，那么倒数第二个0之前的字符串（包含倒数第二个0）都是匹配的
所以主要考察倒数第二个0和最后一个0之间的1的个数：如果是奇数个1，显然无法完成匹配，
所以只能是偶数个1才能完成匹配
'''


class Solution:
    """
    :type bits: List[int]
    :rtype: bool
    """

    def isOneBitCharacter1(self, bits):
        i = 0
        while i < len(bits) - 1:
            i += bits[i] + 1  # 巧妙利用数字的特点，避开if
        return i == len(bits) - 1

    def isOneBitCharacter2(self, bits):
        i = len(bits) - 2
        while i >= 0 and bits[i]: i -= 1  # 找到倒数第二个0
        return (len(bits) - i) % 2 == 0  # 偶数个1则为0


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

        testArgs.append([[1, 0, 0], True])
        testArgs.append([[1, 1, 1, 0], False])

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

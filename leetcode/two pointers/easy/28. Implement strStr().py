__author__ = 'Hk4Fun'
__date__ = '2018/4/9 11:25'
'''题目描述：
Implement strStr().
Return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.

Example 1:
Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:
Input: haystack = "aaaaa", needle = "bba"
Output: -1
'''
'''主要思路：
思路1：时间O（mn），空间O（1）
暴力枚举（双指针）
思路2：时间O（n+m），空间O（n）
KMP
'''


class Solution:
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """

    def strStr_brute_force(self, haystack, needle):
        if needle == '': return 0
        for i in range(len(haystack) - len(needle) + 1):  # 指向主串的指针
            for j in range(len(needle)):  # 指向子串的指针
                if haystack[i + j] != needle[j]:  # 一旦不匹配就退出子串，从主串的下一个开始
                    break
                if j == len(needle) - 1:  # 匹配到子串末尾则匹配成功
                    return i
        return -1

    def strStr_find(self, haystack, needle):  # 有轮子不用？
        return haystack.find(needle)

    # def strStr_KMP(self, haystack, needle):
    #     pass


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

        testArgs.append(['hello', 'll', 2])
        testArgs.append(['aaaaa', 'bba', -1])

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

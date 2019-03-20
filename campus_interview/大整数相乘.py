'''题目来源:
拼多多2018校招
'''
'''题目描述：
有两个用字符串表示的非常大的大整数,算出他们的乘积，也是用字符串表示。不能用系统自带的大整数类型。
输入描述:
空格分隔的两个字符串，代表输入的两个大整数
输出描述:
输入的乘积，用字符串表示
示例：
输入
72106547548473106236 982161082972751393
输出
70820244829634538040848656466105986748
'''
'''主要思路：
还原乘法的过程，按位相乘再乘以位数权重，注意计算位数权重时，数组越往右权重越小
'''


class Solution:
    def multiply(self, a: str, b: str) -> str:
        if not a or not b: return
        if a == '0' or b == '0': return '0'  # 有一个是0则直接返回0
        a_ = a[1:] if a[0] == '-' else a  # 转换成正数
        b_ = b[1:] if b[0] == '-' else b
        res = 0
        for i, v1 in enumerate(a_):
            for j, v2 in enumerate(b_):
                res += int(v1) * int(v2) * pow(10, len(a_) - i - 1 + len(b_) - j - 1)  # 越往右权重越小
        pos = (len(a_) == len(a) and len(b_) == len(b)) or (len(a_) < len(a) and len(b_) < len(b))
        return str(res) if pos else '-' + str(res)  # 返回结果记得添上负号


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = True  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 1  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append(['0', '0', '0'])
        testArgs.append(['0', '-1', '0'])
        testArgs.append(['-1', '0', '0'])
        testArgs.append(['1', '0', '0'])
        testArgs.append(['0', '1', '0'])
        testArgs.append(['1', '1', '1'])
        testArgs.append(['-1', '1', '-1'])
        testArgs.append(['1', '-1', '-1'])
        testArgs.append(['-1', '-1', '1'])
        testArgs.append(['72106547548473106236', '982161082972751393', '70820244829634538040848656466105986748'])
        testArgs.append(['-72106547548473106236', '982161082972751393', '-70820244829634538040848656466105986748'])
        testArgs.append(['-72106547548473106236', '-982161082972751393', '70820244829634538040848656466105986748'])
        return testArgs

    def convert(self, result, *func_arg):
        # 在此处填写转换函数，将测试结果转换成其他形式
        return result

    def checked(self, result, expected, *func_arg):
        # 在此处填写比较器，测试返回的结果是否正确
        return result == expected


if __name__ == '__main__':
    MyTest(Solution()).start_test()

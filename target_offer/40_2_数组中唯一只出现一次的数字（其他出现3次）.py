__author__ = 'Hk4Fun'
__date__ = '2018/3/5 23:36'

'''题目描述：
在一个数组中除了一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。
'''
'''主要思路：
思路1（时间O(n), 空间O(1)）：
位运算。我们把数组中所有数字的二进制表示的每一位都加起来，
如果某一位的和能被3整除，那么那个只出现一次的数字二进制表示中对应的那一位为0，否则为1
思路2（时间O(nlogn), 空间O(1)）：
先排序，则没有连续出现3次的那个数字就是
思路3（时间O(n), 空间O(n)）：
建立哈希表，查表找到出现1次的那个数字

该题可以很容易拓展到“其他数字都出现k次”的情况，其解题思路不变
'''


class Solution:
    def FindNumberAppearingOnce1(self, numbers):
        if not numbers:
            return
        bitSum = [0] * 32
        for num in numbers:
            bitMask = 1
            for j in range(31, -1, -1):
                if num & bitMask:
                    bitSum[j] += 1
                bitMask <<= 1
        result = 0
        for i in range(32):
            result = (result << 1) + (bitSum[i] % 3)  # 注意这里bitSum[i]%3要么为0要么为1，不会出现2
        # python数字类型的特殊性：如果原数为负数，截取后32位导致变为正数，所以需要检查最高位是否为1
        # 为1说明原数为负数，所以需要将最高位左边所有的0变为1，也就是说需要保持右边32位不变而左边所有位取反，
        # 所以可以先把右边32位局部取反，然后整体取反。局部取反可以^0xffffffff，而整体取反直接~
        return result if result >> 31 == 0 else ~(result ^ 0xffffffff)

    def FindNumberAppearingOnce2(self, numbers):
        if not numbers: return
        numbers.sort()
        length = len(numbers)
        for i in range(0, length, 3):
            if i + 1 < length and i + 2 < length and numbers[i] == numbers[i + 1] == numbers[i + 2]:
                continue
            return numbers[i]

    def FindNumberAppearingOnce3(self, numbers):
        if not numbers: return
        map = {}
        for num in numbers:
            map[num] = map.setdefault(num, 0) + 1
        for i, v in map.items():
            if v == 1:
                return i


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[1, 1, 2, 2, 2, 1, 3], 3])
        testArgs.append([[3, 4, 4, 2, 2, 2, 4], 3])
        testArgs.append([[5, 5, 4, 5, 2, 2, 2], 4])
        testArgs.append([[-10, 214, 214, 214], -10])
        testArgs.append([[-209, 3467, -209, -209], 3467])
        testArgs.append([[1024, -1025, 1024, -1025, 1024, -1025, 1023], 1023])
        testArgs.append([[-1024, -1024, -1024, -1023], -1023])
        testArgs.append([[-23, 0, 214, -23, 214, -23, 214], 0])
        testArgs.append([[3467, 0, 0, 0, 0, 0, 0], 3467])
        testArgs.append([[], None])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

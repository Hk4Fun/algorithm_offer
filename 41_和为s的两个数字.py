__author__ = 'Hk4Fun'
__date__ = '2018/2/14 21:19'

'''题目描述：
输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S，
如果有多对数字的和等于S，输出两个数的乘积最小的。
对应每个测试案例，输出两个数，小的先输出。
'''
'''主要思路：
因为当两个数的和一定的时候, 两个数字的差越大, 乘积越小，所以两个数中较小的数一定要从左边开始遍历
思路1（O(n^2)）：暴力枚举。先在数组中从左至右固定每个数字，再依次判断数组中该数字右边的数字与它的
                 和是不是等于s，找到的第一对就是乘积最大的
思路2（O(n^2)）：将s减去数组中的每个数并放进临时数组中，如果存在和为s的数，那么这一对将会在临时数组
                 中出现并交换顺序，且乘积最大的那一对在临时数组头和尾。需要空间复杂度O(n)          
思路3（O(n)）：设置两个指针分别指向第一个和最后一个数，如果它们的和等于s，我们就找到了这两个数；
               如果小于s，由于数组已经排好序，所以只需让较小数的指针往后移；如果大于s，这让较大数
               的指针往前移。最终找到的第一对就是乘积最大的
'''


class Solution:
    def FindNumbersWithSum1(self, array, sum):
        if array:
            for i, v in enumerate(array):
                if sum - v in array[i + 1:]:
                    return [v, sum - v]
        return []

    def FindNumbersWithSum2(self, array, sum):
        if array:
            mirror = [sum - i for i in array]
            filter_array = [i for i in array if i in mirror]
            if len(filter_array) > 1:
                return [filter_array[-1], filter_array[0]]
        return []

    def FindNumbersWithSum3(self, array, sum):
        if array:
            start = 0
            end = len(array) - 1
            while start < end:  # 当 start==end 时，指向同一个数，则不再是不同位置的两个数，结束循环
                if array[start] + array[end] < sum:
                    start += 1
                elif array[start] + array[end] > sum:
                    end -= 1
                else:
                    return [array[start], array[end]]
        return []


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        # 存在和为s的两个数字，这两个数字位于数组的中间
        testArgs.append([[1, 2, 5, 5, 11, 15], 10, {5, 5}])

        # 存在和为s的两个数字，这两个数字位于数组的两端
        testArgs.append([[1, 2, 4, 7, 11, 16], 17, {1, 16}])

        # 存在多对和为s的数字
        testArgs.append([[1, 2, 3, 4, 5, 6], 7, {1, 6}])

        # 存在多对和为s的数字
        testArgs.append([[5, 5, 5, 5, 5, 5], 10, {5, 5}])

        # 不存在和为s的两个数字
        testArgs.append([[1, 2, 5, 7, 11, 16], 10, {}])

        # 只有一个数
        testArgs.append([[1], 1, {}])

        # 空数组
        testArgs.append([[], 10, {}])

        return testArgs

    def convert(self, result, *func_arg):
        return set(result) if result else {}


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

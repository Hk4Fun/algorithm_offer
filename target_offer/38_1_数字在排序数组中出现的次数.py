__author__ = 'Hk4Fun'
__date__ = '2018/2/13 21:14'

'''题目描述：
统计一个数字在排序数组中出现的次数
'''
'''主要思路：
思路1：直接遍历整个数组统计，O(n)
思路2：既然是排好序的，那么自然想到二分法了。总体思路是找到第一个k的位置，再找到最后一个k的位置，相减加一。
       先查找第一个k的位置：如果中间的数字比k大，那么k只可能出现在数组的前半段，下一轮就只在数组的前半段
       查找就可以了。如果中间的数字比k小，那么k只可能出现在数组的后半段，下一轮就只在数组的后半段查找就可以了。
       关键是如果中间的数字等于k呢？我们先判断该数字是不是第一个k。如果中间数字前面不是k，则该中间数字刚好
       就是第一个k；如果中间数字前面也是k，则第一个k肯定在数组前半段，下一轮我们仍然需要在数组前半段查找。O(logn)
思路3：思路2用递归实现，思路3用循环实现，其实没什么区别
思路4：用内置方法count()......
'''


class Solution:
    def GetNumberOfK1(self, data, k):
        return sum(True for i in data if i == k) if data else 0

    def GetNumberOfK2(self, data, k):
        def GetFirstK(data, k, start, end):
            if start > end:
                return -1
            mid = start + ((end - start) >> 1)
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            elif mid > start and data[mid - 1] == k:
                end = mid - 1
            else:
                return mid
            return GetFirstK(data, k, start, end)

        def GetLastK(data, k, start, end):
            if start > end:
                return -1
            mid = start + ((end - start) >> 1)
            if data[mid] > k:
                end = mid - 1
            elif data[mid] < k:
                start = mid + 1
            elif mid < end and data[mid + 1] == k:
                start = mid + 1
            else:
                return mid
            return GetLastK(data, k, start, end)

        if not data:
            return 0
        count = 0
        length = len(data)
        first = GetFirstK(data, k, 0, length - 1)
        last = GetLastK(data, k, 0, length - 1)
        if first > -1:  # first>-1则last>-1
            count = last - first + 1
        return count

    def GetNumberOfK3(self, data, k):
        def firstK(data, k):
            l, r = 0, len(data) - 1
            while l <= r:
                m = l + ((r - l) >> 1)
                if data[m] < k:
                    l = m + 1
                elif data[m] > k:
                    r = m - 1
                else:
                    if m == 0 or data[m - 1] < k:
                        return m
                    else:
                        r = m - 1
            return -1

        def lastK(data, k):
            l, r = 0, len(data) - 1
            while l <= r:
                m = l + ((r - l) >> 1)
                if data[m] < k:
                    l = m + 1
                elif data[m] > k:
                    r = m - 1
                else:
                    if m == len(data) - 1 or data[m + 1] > k:
                        return m
                    else:
                        l = m + 1
            return -1

        if not data: return 0
        first, last = firstK(data, k), lastK(data, k)
        return last - first + 1 if first != -1 else 0

    def GetNumberOfK4(self, data, k):
        return data.count(k) if data else 0


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []
        self.debug = True

        # 查找的数字出现在数组的中间
        testArgs.append([[1, 2, 3, 3, 3, 3, 4, 5], 3, 4])

        # 查找的数组出现在数组的开头
        testArgs.append([[3, 3, 3, 3, 4, 5], 3, 4])

        # 查找的数组出现在数组的结尾
        testArgs.append([[1, 2, 3, 3, 3, 3], 3, 4])

        # 查找的数字不存在
        testArgs.append([[1, 3, 3, 3, 3, 4, 5], 2, 0])

        # 查找的数字比第一个数字还小，不存在
        testArgs.append([[1, 3, 3, 3, 3, 4, 5], 0, 0])

        # 查找的数字比最后一个数字还大，不存在
        testArgs.append([[1, 3, 3, 3, 3, 4, 5], 6, 0])

        # 数组中的数字从头到尾都是查找的数字
        testArgs.append([[3, 3, 3, 3], 3, 4])

        # 数组中的数字从头到尾只有一个重复的数字，不是查找的数字
        testArgs.append([[3, 3, 3, 3], 4, 0])

        # 数组中只有一个数字，是查找的数字
        testArgs.append([[3], 3, 1])

        # 数组中只有一个数字，不是查找的数字
        testArgs.append([[3], 4, 0])

        # 空数组
        testArgs.append([[], 4, 0])

        # None
        testArgs.append([None, 4, 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

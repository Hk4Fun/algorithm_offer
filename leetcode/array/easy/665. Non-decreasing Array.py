__author__ = 'Hk4Fun'
__date__ = '2018/3/30 0:38'
'''题目描述：
Given an array with n integers, your task is to check if 
it could become non-decreasing by modifying at most 1 element.
We define an array is non-decreasing if 
array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example 1:
Input: [4,2,3]
Output: True
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.

Example 2:
Input: [4,2,1]
Output: False
Explanation: You can't get a non-decreasing array by modify at most one element.

Note: The n belongs to [1, 10,000].
'''
'''主要思路：
思路1（时间O（n），空间O（1）, beats 99% ）：      
最多修改一次，那么从左到右扫描数组，看是否存在A[p]>A[p+1]
不存在，说明原数组有序，True；
存在就记录下p，继续检查，若再次出现A[p]>A[p+1]，说明要修改不止一处，False；
确实只出现一次，那么就分情况讨论p周围几个点的情况：
首先已知A[p]>A[p+1]，那么考虑A[p-1]和A[p+2]:
不存在A[p-1]，说明p=0，则只需A[p]下调，令A[p]=A[p+1]，True；
不存在A[p+2]，说明p=len(A)-2，则只需A[p+1]上调，令A[p+1]=A[p]，True；
都存在，则情况稍微复杂，画图如下：
                          p+2
-------------p---------p+2-----------
         p-1        p+2
------p-1--------p+1-----------------
   p-1
A[p-1]和A[p+2]各有两种情况：
A[p+1]<A[p-1]<A[p]和A[p-1]<=A[p+1]
A[p+1]<A[p+2]<A[p]和A[p+2]>=A[p]
可以看到，当A[p-1]和A[p+2]同时在A[p+1]和A[p]之间时，调整一次是不可能有序的，False;
其他情况下，要么A[p-1]<=A[p+1]，此时只需A[p]下调，令A[p]=A[p+1]，True;
要么A[p+2]>=A[p]，此时只需A[p+1]上调，令A[p+1]=A[p]，True


思路2（时间O（nlogn），空间O（n））：
这个思路很好理解：
在遇到A[p]>A[p+1]时，要么A[p]下调， 要么A[p+1]上调，那么可以拷贝两个数组，
一个尝试上调，一个尝试下调，然后都排序看一下是否还相等，有一个相等说明调整成功，
确实只需调整一次；都不成功则说明无论上调还是下调都无法一次做到有序

'''


class Solution:
    def checkPossibility1(self, A):
        p = None
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                if p is not None: return False
                p = i
        return (p is None or p == 0 or p == len(A) - 2 or
                A[p - 1] <= A[p + 1] or A[p] <= A[p + 2])

    def checkPossibility2(self, A):
        copy1, copy2 = A[:], A[:]
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                copy1[i] = A[i + 1]  # 尝试下调
                copy2[i + 1] = A[i]  # 尝试上调
                break  # 只调整一次
        return copy1 == sorted(copy1) or copy2 == sorted(copy2)


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

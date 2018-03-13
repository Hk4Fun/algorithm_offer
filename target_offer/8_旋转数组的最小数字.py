__author__ = 'Hk4Fun'
__date__ = '2018/1/3 1:46'

'''题目描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
'''
'''主要思路：
部分排序，则可用二分查找，注意在等于的时候让high-1，顺序查找，退化成O(n)
（注意到[1,0,1,1,1]和[1,1,1,0,1]的区别，此时无法判断最小值在哪边，故只能用顺序查找）：
(1)array[mid] > array[high]:
出现这种情况的array类似[3,4,5,6,0,1,2]，此时最小数字一定在mid的右边。
low = mid + 1
(2)array[mid] == array[high]:
出现这种情况的array类似 [1,0,1,1,1] 或者[1,1,1,0,1]，此时最小数字不好判断在mid左边
还是右边,这时只好一个一个试
high = high - 1
(3)array[mid] < array[high]:
出现这种情况的array类似[2,2,3,4,5,6,6],此时最小数字一定就是array[mid]或者在mid的左
边。因为右边必然都是递增的。
若 mid = 0 ,这说明low与high之间未发生旋转，最小数字就是array[mid]，
或者array[mid-1]>array[mid]，则最小数字就是array[mid]；
否则mid不为零且array[mid-1]<=array[mid]，最小数字在mid的左边，
high = mid - 1
'''


class Solution:

    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return
        low, high = 0, len(rotateArray) - 1
        while low < high:
            mid = low + ((high - low) >> 1)
            if rotateArray[mid] > rotateArray[high]:
                low = mid + 1
            elif rotateArray[mid] < rotateArray[high]:
                if mid == 0 or rotateArray[mid - 1] > rotateArray[mid]:
                    return rotateArray[mid]
                else:
                    high = mid - 1
            else:
                high = high - 1  # 退化成O(n)
        return rotateArray[low] # 最终一定是high==low跳出循环

    # ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        testArgs = []
        testArgs.append([[3, 4, 5, 1, 2], 1])  # 典型输入，单调升序的数组的一个旋转
        testArgs.append([[3, 4, 5, 1, 1, 2], 1])  # 有重复数字，并且重复的数字为最小的数字
        testArgs.append([[3, 4, 5, 5, 1, 2], 1])  # 有重复数字，并且重复的数字为最大的数字
        testArgs.append([[3, 4, 5, 1, 2, 2], 1])  # 有重复数字，但重复的数字不是最小数字和最大数字
        testArgs.append([[1, 0, 1, 1, 1], 0])  # 特殊情况，测试顺序顺序查找
        testArgs.append([[1, 1, 1, 0, 1], 0])  # 同上
        testArgs.append([[1, 2, 3, 4, 5], 1])  # 单调升序数组，旋转0个元素，也就是单调升序数组本身
        testArgs.append([[2], 2])  # 数组中只有一个数字
        testArgs.append([[], None])  # 空数组

        return testArgs


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

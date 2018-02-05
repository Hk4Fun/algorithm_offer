__author__ = 'Hk4Fun'
__date__ = '2018/1/3 1:46'

'''题目描述：
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
'''
'''主要思路：
部分排序，则可用二分查找，left指向头，right指向尾，
a[left]应大于等于a[right]，否则a[0]就是最小值（未发生旋转）
a[mid]>=a[left]时，说明最小值在右边，a[mid]<=a[right]时，说明最小值在左边
left一直在左边有序序列中，而right一直在右边有序序列
最终right-left=1时，最小值为a[right]
特殊情况：a[left]=a[mid]=a[right]
注意到[1,0,1,1,1]和[1,1,1,0,1]的区别，此时无法判断最小值在哪边，
故只能用顺序查找，可直接调用min()
'''


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        if not rotateArray:
            return
        left, right = 0, len(rotateArray) - 1
        while rotateArray[left] >= rotateArray[right]:
            if right - left == 1:
                return rotateArray[right]
            mid = (left + right) // 2  # 注意mid只能为整数
            if rotateArray[left] == rotateArray[mid] == rotateArray[right]:
                return min(rotateArray)
            elif rotateArray[mid] >= rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
        return rotateArray[0]


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

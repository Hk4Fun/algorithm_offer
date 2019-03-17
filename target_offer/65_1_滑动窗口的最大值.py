__author__ = 'Hk4Fun'
__date__ = '2018/2/26 19:41'

'''题目描述：
给定一个数组和滑动窗口的大小k，找出所有滑动窗口里数值的最大值。
例如，如果输入数组{2,3,4,2,6,2,5,1}及滑动窗口的大小3，那么一共存在6个滑动窗口，
他们的最大值分别为{4,4,6,6,6,5}；
针对数组{2,3,4,2,6,2,5,1}的滑动窗口有以下6个：
{[2,3,4],2,6,2,5,1}， {2,[3,4,2],6,2,5,1}， {2,3,[4,2,6],2,5,1}， 
{2,3,4,[2,6,2],5,1}， {2,3,4,2,[6,2,5],1}， {2,3,4,2,6,[2,5,1]}。
'''
'''主要思路：
思路1（时间复杂度O（nk），空间复杂度O（1））：
遍历求出每个窗口的最大值

思路2（时间复杂度O（nk），空间复杂度O（1））：
思路1的简化。注意到，当窗口往右移1格时，如果新加入的数大于等于原来窗口的最大值，
那么新窗口的最大值当然就是这个新加入的数；否则看那个被淘汰的数是不是原窗口的最大值，
是的话说明最大值只能在新窗口中；如果以上条件都不满足，说明新加入的数没有原窗口最大值大，
且原窗口的最大值也没被淘汰，则最大值不变。

思路3（时间复杂度O（n），空间复杂度O（n））：
用一个双端队列，其中保存当前可能为最大值的数的下标，每当窗口滑动一次
1.新增加的值从队尾开始比较，把前面所有小于等于它的值从队尾取出，直到遇到比它大的数就停止：
  因为这些数已经不再可能成为后面滑动窗口的最大值了，有种‘长江后浪推前浪’的感觉。
  注意等于的数也要淘汰，因为后来的数已经与前面的数同窗口，肯定比前面等于它的数要被晚淘汰。
  新来的数会淘汰掉前面小于等于它的数，而如果前面的数比它大则自己没有资格淘汰前面的数，更别说更前面的数。
  但该数还是有‘潜质’成为最大数的，因为可能由于前面的数被滑动窗口的移动而强行淘汰使得自己成为最大数，所以会进入队尾等待‘考核’。
2.判断当前最大值是否过期，过期则从队首取出：
  当一个数字的下标与当前正在处理的数字的下标之差大于等于滑动窗口大小时，
  该最大值过期，即已经从窗口中滑出，需要从队首删除。滑动窗口总是要往右移的，
  再大的数也会被淘汰。
每次通过以上两步操作使得队列第一个位置为当前窗口的最大值

思路4（时间复杂度O（nlogn），空间复杂度O（n））：
由于求每次窗口最大值，所以可以用最大堆实现。但存在堆中的每个数据为（值，下标），
堆按照每个元组的第一个元素来排序
'''
from heapq import heappush, heappop
from collections import deque


class Solution:
    def maxInWindows1(self, num, size):
        if not num or not size or size > len(num) or size < 1:
            return []
        return [max(num[i:i + size]) for i in range(len(num) - size + 1)]

    def maxInWindows2(self, num, size):
        if not num or not size or size > len(num) or size < 1:
            return []
        cur_max = max(num[:size])
        res = [cur_max]
        for i in range(size, len(num)):
            if num[i] >= cur_max:
                cur_max = num[i]
            elif num[i - size] == cur_max:
                cur_max = max(num[i - size + 1:i + 1])
            res.append(cur_max)
        return res

    def maxInWindows3(self, num, size):
        if not num or not size or size > len(num) or size < 1:
            return []
        queue = deque()
        res = []
        for i in range(len(num)):
            # 新增加的值从队尾开始比较，把前面所有小于等于它的值从队尾取出，直到遇到比它大的数就停止
            while queue and num[i] >= num[queue[-1]]:
                queue.pop()
            # 判断当前最大值是否过期，过期则从队首取出
            # 由于一次只移动一个位置，所以只能淘汰掉一个数，一个if就可以，不需要while
            if queue and i - queue[0] == size:
                queue.popleft()
            # 进入队列的是数的下标
            queue.append(i)
            # 当处理数据下标（从0开始）等于size-1时开始写入窗口最大值，
            # 因为此时刚好来到第一个窗口的尾部，产生第一个最大值，之后窗口开始移动
            if i >= size - 1:
                # 每次通过以上两步操作使得队列第一个位置为当前窗口的最大值
                res.append(num[queue[0]])
        return res

    def maxInWindows4(self, num, size):
        if not num or not size or size > len(num) or size < 1:
            return []
        res, maxHeap = [], []
        for i, v in enumerate(num):
            heappush(maxHeap, (-v, i))
            if maxHeap and i - maxHeap[0][1] >= size:
                heappop(maxHeap)
            if i >= size - 1:
                res.append(-maxHeap[0][0])
        return res


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug模式下每个测试用例只测试一遍，默认情况下关闭debug模式
        testArgs = []
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs.append([[2, 3, 4, 2, 6, 2, 5, 1], 3, [4, 4, 6, 6, 6, 5]])  # 功能测试
        testArgs.append([[1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]])  # 功能测试
        testArgs.append([[1, 3, 5, 7, 9, 11, 13, 15], 4, [7, 9, 11, 13, 15]])  # 递增序列
        testArgs.append([[16, 14, 12, 10, 8, 6, 4], 5, [16, 14, 12]])  # 递减序列
        testArgs.append([[3, 3, 3, 3, 3, 3, 3, 3], 5, [3, 3, 3, 3]])  # 数据相同
        testArgs.append([[10, 14, 12, 11], 1, [10, 14, 12, 11]])  # 窗口大小为1
        testArgs.append([[3, 3, 3, 3, 3, 3, 3, 3], 1, [3, 3, 3, 3, 3, 3, 3, 3]])  # 数据相同，一个窗口
        testArgs.append([[10, 14, 12, 11], 4, [14]])  # 窗口大小为数据长度
        testArgs.append([[10, 14, 12, 11], 0, []])  # 窗口大小为0
        testArgs.append([[10, 14, 12, 11], 5, []])  # 窗口大小大于数据长度
        testArgs.append([[], 2, []])  # 空数组
        testArgs.append([None, None, []])  # None

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

__author__ = 'Hk4Fun'
__date__ = '2018/2/11 16:38'

'''题目描述：
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。
输入一个数组, 求出这个数组中逆序对的总数
'''
'''主要思路：
思路1：暴力枚举。每遍历到一个数字就逐个比较该数字与它后面数字的大小。
       如果后面的数字比它小，则这两个数字就组成一个逆序对。时间复杂度明显是O(n^2)
思路2：归并排序，在合并时统计逆序对个数。设合并的两个数组为a1和a2，用两个指针p1，p2
       指向a1和a2的末尾元素，并每次比较两个指针指向的数字。如果p1数字大于p2，则构成
       逆序对，并且逆序对的数目等于p2之前的元素个数(包括p2指向的元素)，因为a2是已经
       排好序的，则p2之前的数都小于p1指向的数。反之，如果p1数字小于等于p2，则不构成
       逆序对。每一次比较都把较大的数从后往前复制到一个辅助数组里,确保辅助数组里的数字
       是递增排序的。然后把较大的数的指针往前移一位，进行下一轮比较。所以总的逆序对数就是
       先把数组分隔成子数组，先统计出两个子数组内部的逆序对数，然后统计出两个相邻子数组之间的
       逆序对数，三者之和。
思路3：先把原数组进行从小到大排序，得到一个排好序的数组。然后遍历排序数组，
       找到每个数在原数组的索引，该索引就是这个数的在原数组中相对排好序的数组的偏移，
       那么偏移多少就有多少由于该数的偏移造成的逆序对。记得每找一次索引就要把该数从原数组中
       移除，保证接下原数组每个数的偏移是正确的。注意，排好序的数组一直在往后遍历，
       相当于排好序的数组也一直在更新，类似一个递归的过程，只不过用循环来完成。
'''


class Solution:
    # 暴力枚举
    def InversePairs1(self, data):
        count = 0
        length = len(data)
        for i in range(length):
            for j in range(i + 1, length):
                if data[i] > data[j]:
                    count += 1
        return count

    # 归并排序
    def InversePairs2(self, data):
        def InversePairsCore(data, copy, start, end):
            if start == end:
                return 0
            mid = (end - start) >> 1
            # 注意这里的copy和data位置交换了，这样就能保证递归回来时，上一层拿到的data是下一层已经排好序的copy
            left = InversePairsCore(copy, data, start, start + mid)
            right = InversePairsCore(copy, data, start + mid + 1, end)

            # i初始化为前半段最后一个数字的下标
            i = start + mid
            # j初始化为后半段最后一个数字的下标
            j = end

            indexCopy = end
            count = 0
            while i >= start and j >= start + mid + 1:
                # 复制的时候统计两个子数组之间的逆序对数
                if data[i] > data[j]:
                    copy[indexCopy] = data[i]
                    indexCopy -= 1
                    i -= 1
                    count += j - start - mid  # 逆序对的数目等于j之前的元素个数(包括j指向的元素)
                else:
                    copy[indexCopy] = data[j]
                    indexCopy -= 1
                    j -= 1
            # 将剩下的移到辅助数组里
            while i >= start:
                copy[indexCopy] = data[i]
                indexCopy -= 1
                i -= 1
            while j >= start + mid + 1:
                copy[indexCopy] = data[j]
                indexCopy -= 1
                j -= 1
            return left + right + count

        if not data:
            return 0
        copy = data[:]
        return InversePairsCore(data, copy, 0, len(data) - 1)

    # 排序后利用下标的特点
    def InversePairs3(self, data):
        count = 0
        copy = sorted(data[:])
        for num in copy:
            count += data.index(num)
            data.remove(num)
        return count


# ================================测试代码================================
from Test import Test


class MyTest(Test):
    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案

        testArgs = []

        testArgs.append([[1, 2, 3, 4, 7, 6, 5], 3])

        # 递减排序数组
        testArgs.append([[6, 5, 4, 3, 2, 1], 15])

        # 递增排序数组
        testArgs.append([[1, 2, 3, 4, 5, 6], 0])

        # 数组中只有一个数字
        testArgs.append([[1], 0])

        # 数组中只有两个数字，递增排序
        testArgs.append([[1, 2], 0])

        # 数组中只有两个数字，递减排序
        testArgs.append([[2, 1], 1])

        # 数组中有相等的数字
        testArgs.append([[1, 2, 1, 2, 1], 3])

        # 空数组
        testArgs.append([[], 0])

        # 大数测试
        testArgs.append([[[364, 637, 341, 406, 747, 995, 234, 971, 571, 219, 993, 407, 416, 366, 315, 301, 601, 650,
                           418, 355, 460, 505, 360, 965, 516, 648, 727, 667, 465, 849, 455, 181, 486, 149, 588, 233,
                           144, 174, 557, 67, 746, 550, 474, 162, 268, 142, 463, 221, 882, 576, 604, 739, 288, 569, 256,
                           936, 275, 401, 497, 82, 935, 983, 583, 523, 697, 478, 147, 795, 380, 973, 958, 115, 773, 870,
                           259, 655, 446, 863, 735, 784, 3, 671, 433, 630, 425, 930, 64, 266, 235, 187, 284, 665, 874,
                           80, 45, 848, 38, 811, 267, 575]], 0])

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

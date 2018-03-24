__author__ = 'Hk4Fun'
__date__ = '2018/3/23 1:25'
'''
http://ox186n2j0.bkt.clouddn.com/sorting.png
'''
from random import shuffle


class Solution:
    def bubble(self, arr):
        for i in range(1, len(arr)):
            for j in range(len(arr) - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr

    def bubble_flag(self, arr):
        for i in range(1, len(arr)):
            exchange = False
            for j in range(len(arr) - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    exchange = True
            if not exchange: break  # 一趟下来没有发生交换则证明已经有序，停止排序
        return arr

    def selection(self, arr):
        for i in range(len(arr)):
            minIndex = i
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            if minIndex != i:  # 最小值下标没有移动就不用交换
                arr[i], arr[minIndex] = arr[minIndex], arr[i]
        return arr

    def insertion(self, arr):
        for i in range(1, len(arr)):  # 从下标1开始
            preIndex = i - 1
            cur = arr[i]
            while preIndex >= 0 and arr[preIndex] > cur:
                arr[preIndex + 1] = arr[preIndex]
                preIndex -= 1
            arr[preIndex + 1] = cur
        return arr

    def insertion_sentinel(self, arr):
        exchange = False  # 模仿冒泡排序设置exchange
        for i in range(len(arr) - 1, 0, -1):  # 将最小值冒泡到最前面做哨兵，这样就不用担心preIndex的越界
            if arr[i] < arr[i - 1]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                exchange = True
        if not exchange: return  # 一趟下来没有发生交换则证明已经有序，停止排序

        for i in range(2, len(arr)):  # 从下标2开始
            preIndex = i - 1
            cur = arr[i]
            while arr[preIndex] > cur:  # 注意到这里不用控制preIndex >= 0
                arr[preIndex + 1] = arr[preIndex]
                preIndex -= 1
            arr[preIndex + 1] = cur
        return arr

    def insertion_binary(self, arr):
        for i in range(1, len(arr)):
            cur = arr[i]
            low, high = 0, i
            while low < high:  # 二分查找从左往右第一个大于cur的数
                mid = low + ((high - low) >> 1)
                if arr[mid] > cur:  # 大于不-1，因为这个位置可能就是第一个大于cur的数
                    high = mid
                else:  # 小于等于直接+1，因为这个位置不可能就是第一个大于cur的数
                    low = mid + 1
            for j in range(i, low, -1):  # 把大于cur的数都后移1位
                arr[j] = arr[j - 1]
            arr[low] = cur  # cur放进出的位置
        return arr

    def shell(self, arr):
        gap = len(arr) // 3
        while gap > 0:
            # 内循环就是插入排序，只不过增量为gap
            for i in range(gap, len(arr)):
                preIndex = i - gap
                cur = arr[i]
                while preIndex >= 0 and arr[preIndex] > cur:
                    arr[preIndex + gap] = arr[preIndex]
                    preIndex -= gap
                arr[preIndex + gap] = cur
            gap //= 3
        return arr

    def merge_u2d_1(self, arr):  # u2d：up-to-down，自顶向下
        # 容易理解但是发生多次数组的复制
        def merge(left, right):
            res = []
            while left and right:
                if left[0] <= right[0]:
                    res.append(left.pop(0))
                else:
                    res.append(right.pop(0))
            while left:
                res.append(left.pop(0))
            while right:
                res.append(right.pop(0))
            return res

        if len(arr) < 2:
            return arr
        mid = len(arr) >> 1
        return merge(self.merge_u2d_1(arr[:mid]), self.merge_u2d_1(arr[mid:]))

    def merge_u2d_2(self, arr):
        # 不好理解，但只需复制数组一次
        def merge(arr, copy, low, mid, high):
            # 注意这里是吧arr放进copy中
            i, j = low, mid + 1
            for k in range(low, high + 1):
                if i > mid:
                    copy[k] = arr[j]
                    j += 1
                elif j > high:
                    copy[k] = arr[i]
                    i += 1
                elif arr[i] <= arr[j]:
                    copy[k] = arr[i]
                    i += 1
                else:
                    copy[k] = arr[j]
                    j += 1

        def sort(arr, copy, low, high):
            if low < high:
                mid = low + ((high - low) >> 1)
                # 类似后序遍历
                sort(copy, arr, low, mid)  # 注意这里copy和arr的位置调换了一下，可以省去复制arr的时间
                sort(copy, arr, mid + 1, high)
                merge(arr, copy, low, mid, high)

        copy = arr[:]  # 只需复制一次
        sort(arr, copy, 0, len(arr) - 1)
        return copy

    def merge_d2u(self, arr):  # d2u：down-to-up，自底向上
        def merge(arr, low, mid, high):
            copy[low: high + 1] = arr[low: high + 1]  # 把arr放进copy中
            i, j = low, mid + 1
            for k in range(low, high + 1):  # 再从copy中merge到arr
                # 注意这里是把copy放到arr中
                if i > mid:
                    arr[k] = copy[j]
                    j += 1
                elif j > high:
                    arr[k] = copy[i]
                    i += 1
                elif copy[i] <= copy[j]:
                    arr[k] = copy[i]
                    i += 1
                else:
                    arr[k] = copy[j]
                    j += 1

        copy = arr[:]
        size = 1
        while size < len(arr):
            for low in range(0, len(arr) - size, size * 2):
                merge(arr, low, low + size - 1, min(low + size * 2 - 1, len(arr) - 1))
            size += size
        return arr

    def quick(self, arr):
        def partition(arr, left, right):
            i, j = left, right
            pivot = arr[left]  # 选择首位作为枢轴
            while i < j:
                while i < j and arr[j] > pivot: j -= 1
                if i < j:
                    arr[i] = arr[j]
                    i += 1
                while i < j and arr[i] < pivot: i += 1
                if i < j:
                    arr[j] = arr[i]
                    j -= 1
            arr[i] = pivot
            return i

        def quick(arr, left, right):
            if left < right:
                # 类似前序遍历
                index = partition(arr, left, right)
                quick(arr, left, index - 1)
                quick(arr, index + 1, right)

        # shuffle(arr) # 使用shuffle随机打乱数组规律，但这样反而影响了排序的效率？
        quick(arr, 0, len(arr) - 1)
        return arr

    def quick_3way(self, arr):   # 三向切分，荷兰国旗问题，对于含有较多重复字符的排序效率高
        def quick(arr, left, right):
            if left < right:
                pivot = arr[left]  # 选择首位作为枢轴，先记录下来，因为后面会被交换
                lt, gt = left, right  # lt指向第一个等于枢轴的数， gt指向待确定区的最后一个元素，即大于区的前面那个数
                i = left + 1  # i指向待定区的第一个元素
                while i <= gt:
                    if arr[i] < pivot:  # 小于枢轴，则交换后lt和i都往后移一位
                        arr[i], arr[lt] = arr[lt], arr[i]
                        lt += 1
                        i += 1
                    elif arr[i] > pivot:  # 大于枢轴，则交换后只把gt往前移一位，i不动，因为换过来的数是待定区的数
                        arr[i], arr[gt] = arr[gt], arr[i]
                        gt -= 1
                    else:
                        i += 1  # 等于枢轴则i后移一位即可不用交换
                # 现在 arr[left:lt-1] < arr[lt:gt] = pivot < arr[gt+1:right]
                quick(arr, left, lt - 1)
                quick(arr, gt + 1, right)

        # shuffle(arr) # 使用shuffle随机打乱数组规律，但这样反而影响了排序的效率？
        quick(arr, 0, len(arr) - 1)
        return arr

    def quick_2way(self, arr):  # 将等于区和大于区合并，其实与quick()一样
        def partition(arr, left, right):
            # arr[left]作为枢轴,到最后再换过去
            lt = i = left + 1  # lt指向小于区的右边，i指向待定区，一开始都一样
            while i <= right:
                if arr[i] < arr[left]:
                    arr[i], arr[lt] = arr[lt], arr[i]
                    lt += 1
                i += 1
            # 现在pivot=arr[left],arr[left+1:lt-1]<arr[lt:]
            arr[lt - 1], arr[left] = arr[left], arr[lt - 1]  # 注意和lt-1交换
            return lt - 1

        def quick(arr, left, right):
            if left < right:
                # 类似前序遍历
                index = partition(arr, left, right)
                quick(arr, left, index - 1)
                quick(arr, index + 1, right)

        # shuffle(arr) # 使用shuffle随机打乱数组规律，但这样反而影响了排序的效率？
        quick(arr, 0, len(arr) - 1)
        return arr

    def heap_max(self, arr):
        def heapify(arr, i, end):  # 将arr[i]下沉（sink）至合适位置，下沉范围小于end
            # 下沉操作：如果该结点比两个子结点都大就结束下沉，否则选择子结点中最大那个交换来下沉
            while True:
                left = 2 * i + 1  # 注意arr下标是从0开始的，所以这里多加一个1
                right = left + 1
                largest = i
                if left < end and arr[left] > arr[largest]:
                    largest = left
                if right < end and arr[right] > arr[largest]:
                    largest = right
                if largest == i: break  # 最大就是自己，则结束下沉
                arr[i], arr[largest] = arr[largest], arr[i]  # 否则和最大子结点交换
                i = largest  # 继续下沉

        for i in range(len(arr) // 2, -1, -1):  # 先建最大堆
            heapify(arr, i, len(arr))
        for end in range(len(arr) - 1, 0, -1):  # 注意end到1就可以结束了，剩arr[0]一定是最小的
            arr[0], arr[end] = arr[end], arr[0]  # 把堆顶的最大值与参与堆排的数组末尾交换
            heapify(arr, 0, end)  # 然后把刚交换到堆顶的数下沉至合适位置
        return arr


# ================================测试代码================================


from Test import Test


class MyTest(Test):
    def my_test_code(self):
        self.debug = False  # debug为True时每个测试用例只测试一遍，默认情况下关闭debug模式
        self.TEST_NUM = 5  # 单个测试用例的测试次数, 只有在debug为False的情况下生效
        testArgs = []

        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def correct(arr):
            return sorted(arr)

        import random
        arrLen = 100
        arrNum = 100
        numLimit = 100
        for i in range(arrNum):
            arr = []
            for j in range(arrLen):
                arr.append(random.randint(-numLimit, numLimit))
            testArgs.append([arr, correct(arr)])

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

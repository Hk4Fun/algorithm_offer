__author__ = 'Hk4Fun'
__date__ = '2018/2/26 0:35'

'''题目描述：
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。
'''
'''主要思路：
构建大根堆和小根堆，则插入O(logn)，取中位数O(1)
如果用一个数组存储所有到来数据，然后在取中位数时排序返回，则插入O(1)，取中位数O(nlogn)
由此可见，动态构建大根堆和小根堆相当于把排序时间平摊到每次插入操作中，这样在获取中位数时可以O(1)
有两个条件要满足：
1、保证数据平均分配到两个堆中，即两个堆中数据的数目之差不能超过1；
2、保证大根堆里所有数据都要小于小根堆中的数据
由此产生两种思路：
思路1：若数小于等于大堆最大数（堆顶），则插入大堆中，否则插入小堆中；
       之后若大堆比小堆个数多2，则从大堆中弹出堆顶元素并插入到小堆中，
       保证总数个数为偶数时平均分配；
       若小堆比大堆个数多1，则从小堆弹出堆顶元素并插入大堆中，
       保证总数个数为奇数时中位数在大堆堆顶
       之后取数时若大堆元素个数等于小堆元素个数就取大堆堆顶和小堆堆顶的平均值；
       若大堆元素个数和小堆元素个数不等时就取大堆堆顶
思路2：当数据总数（包括当前数）为奇数时，新加入的元素，应当进入大根堆，
       注意不是直接进入大根堆，而是经小根堆筛选后取小根堆中最大元素进入大根堆；
       当数据总数（包括当前数）为偶数时，新加入的元素，应当进入小根堆，
       注意不是直接进入小根堆，而是经大根堆筛选后取大根堆中最大元素进入小根堆
       取数时若总数个数为奇数则直接取大堆堆顶，偶数时取两堆堆顶平均值
这里构建堆用heapq，其构建的都是小根堆（优先队列），所以为了构建大根堆需要在存数取数时加上负号
'''
import heapq


class Heap:
    def __init__(self):
        self._data = []

    @property
    def size(self):
        return len(self._data)

    @property
    def max(self):
        if self.size > 0:
            return self._data[0]

    def push(self, val):
        self._data.append(val)
        self._siftup(self.size - 1)

    def pushpop(self, val):  # 比单纯的push然后pop要快
        if self.size > 0 and val < self.max:
            self._data[0], val = val, self._data[0]
            self._siftdown(0)
        return val

    def _siftup(self, k):  # takes O(logn) time
        while k > 0 and self._data[self._parent(k)] < self._data[k]:
            self._swap(self._parent(k), k)
            k = self._parent(k)

    def _siftdown(self, k):  # takes O(logn) time
        while self._left_child(k) < self.size:
            j = self._left_child(k)
            if (self._right_child(k) < self.size and
                    self._data[self._right_child(k)] > self._data[self._left_child(k)]):
                # j 为左右孩子中较大者
                j += 1
            if self._data[k] >= self._data[j]:  # k 比两个孩子都大就结束下沉
                break
            self._swap(k, j)
            k = j

    def _parent(self, idx):
        return (idx - 1) // 2

    def _left_child(self, idx):
        return 2 * idx + 1

    def _right_child(self, idx):
        return 2 * idx + 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]


class Solution:
    # 返回data中每增加一个数后的中位数序列列表
    def StreamMedian1(self, data):
        def Insert(num):
            if not maxHeap or -num >= maxHeap[0]:  # 加上负号构建大顶堆，所以比较符号也要改变方向
                heapq.heappush(maxHeap, -num)  # 小于等于大堆最大数（堆顶），则插入大堆中
            else:  # 否则插入小堆中
                heapq.heappush(minHeap, num)
            # 保证总数个数为偶数时平均分配
            if len(maxHeap) - len(minHeap) == 2:  # 若大堆比小堆个数多2
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))  # 则从大堆中弹出堆顶元素并插入到小堆中
            # 保证总数个数为奇数时中位数在大堆堆顶
            if len(minHeap) - len(maxHeap) == 1:  # 若小堆比大堆个数多1
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))  # 则从小堆弹出堆顶元素并插入大堆中

        def GetMedian():
            return (-maxHeap[0] + minHeap[0]) / 2 if len(maxHeap) == len(minHeap) else -maxHeap[0]

        if data:
            maxHeap = []
            minHeap = []
            result = []
            for num in data:
                Insert(num)
                result.append(GetMedian())
            return result

    def StreamMedian2(self, data):
        def Insert(num):
            self.count += 1  # 先计数
            if self.count & 1:  # 奇数时，新加入的元素应当进入大根堆
                # 注意不是直接进入大根堆，而是经小根堆筛选后取小根堆中最小元素进入大根堆
                heapq.heappush(maxHeap, -heapq.heappushpop(minHeap, num))
            else:  # 偶数时，新加入的元素，应当进入小根堆
                # 注意不是直接进入小根堆，而是经大根堆筛选后取大根堆中最大元素进入小根堆
                heapq.heappush(minHeap, -heapq.heappushpop(maxHeap, -num))

        def GetMedian():
            return -maxHeap[0] if self.count & 1 else (-maxHeap[0] + minHeap[0]) / 2

        if data:
            self.count = 0  # 计数器
            maxHeap = []
            minHeap = []
            result = []
            for num in data:
                Insert(num)
                result.append(GetMedian())
            return result

    def StreamMedian3(self, data):
        """使用自定义MaxHeap"""

        def Insert(num):
            self.count += 1
            if self.count & 1:
                maxHeap.push(-minHeap.pushpop(-num))
            else:
                minHeap.push(-maxHeap.pushpop(num))

        def GetMedian():
            return maxHeap.max if self.count & 1 else (maxHeap.max + -minHeap.max) / 2

        if data:
            self.count = 0  # 计数器
            maxHeap, minHeap = Heap(), Heap()
            res = []
            for num in data:
                Insert(num)
                res.append(GetMedian())
            return res


# ================================测试代码================================
from Test import Test


class MyTest(Test):

    def my_test_code(self):
        # 只需在此处填写自己的测试代码
        # testArgs中每一项是一次测试，每一项由两部分构成
        # 第一部分为被测试函数的参数，第二部分只有最后一个，为正确答案
        def correct(data):
            # 使用绝对正确但是复杂度不好的方法作为验证，可以调用内置方法验证
            if data:
                result = []
                tmp = []
                for num in data:
                    tmp.append(num)
                    tmp.sort()
                    length = len(tmp)
                    result.append(tmp[length >> 1] if length % 2 else (tmp[length >> 1] + tmp[(length >> 1) - 1]) / 2)
                return result

        self.debug = True
        testArgs = []

        data = [5, 2, 3, 4, 1, 6, 7, 0, 8, 9]  # 无序
        testArgs.append([data, correct(data)])
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 递增
        testArgs.append([data, correct(data)])
        data = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # 递减
        testArgs.append([data, correct(data)])
        testArgs.append([[1], [1]])  # 一个数
        testArgs.append([[], None])  # 空数组
        testArgs.append([None, None])  # None

        # 随机数据测试
        import random
        limit = 100
        length = 100
        test_num = 100
        data = []
        for i in range(test_num):
            for j in range(random.randint(1, length)):
                data.append(random.randint(-limit, limit))
            testArgs.append([data, correct(data)])
            data = []

        return testArgs

    def convert(self, result, *func_arg):
        return result


if __name__ == '__main__':
    solution = Solution()
    MyTest(solution=solution).start_test()

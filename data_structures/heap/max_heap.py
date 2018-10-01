__author__ = 'Hk4Fun'
__date__ = '2018/9/30 19:51'

from dynamic_array import DynamicArray
from exceptions import EmptyError


class MaxHeap:
    def __init__(self, vals=None, capacity=0):
        if vals:
            self._data = DynamicArray(vals)
            self._heapify()
        else:
            self._data = DynamicArray(capacity=capacity)

    def __repr__(self):
        return 'MaxHeap([{}])'.format(','.join(str(i) for i in self._data))

    @property
    def size(self):
        return len(self._data)

    @property
    def max(self):
        if self.size > 0:
            return self._data[0]
        raise EmptyError('Can not get max when heap is empty')

    def is_empty(self):
        return self.size == 0

    def push(self, val):
        self._data.append(val)
        self._siftup(self.size - 1)

    def pop(self):
        ret = self.max
        self._swap(0, self.size - 1)
        self._data.pop()
        self._siftdown(0)
        return ret

    def pushpop(self, val):  # 比单纯的push然后pop要快
        if self.size > 0 and val < self.max:
            self._data[0], val = val, self._data[0]
            self._siftdown(0)
        return val

    def replace(self, val):  # 取出堆中的最大元素，并且替换成val
        # replace 与 pushpop 的区别在于 pushpop 总是返回包含val在内的最大值，
        # 而 replace 返回的是不包括val在内，只在heap中的最大值
        # 也就是说 replace 的返回值可能比val小，而 pushpop 返回值总是大于等于val
        # 以下逻辑等价于 pushpop:
        # if val < self.max:
        #     val = self.replace(val)
        # return val
        ret = self.max
        self._data[0] = val
        self._siftdown(0)
        return ret

    def _heapify(self): # takes O(n) time
        for i in range(self.size // 2 - 1, -1, -1):
            self._siftdown(i)

    def _siftup(self, k): # takes O(logn) time
        while k > 0 and self._data[self._parent(k)] < self._data[k]:
            self._swap(self._parent(k), k)
            k = self._parent(k)

    def _siftdown(self, k): # takes O(logn) time
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
        if idx == 0:
            raise IndexError("index-0 doesn't have parent")
        return (idx - 1) // 2

    def _left_child(self, idx):
        return 2 * idx + 1

    def _right_child(self, idx):
        return 2 * idx + 2

    def _swap(self, i, j):
        self._data[i], self._data[j] = self._data[j], self._data[i]

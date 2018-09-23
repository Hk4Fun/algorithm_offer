__author__ = 'Hk4Fun'
__date__ = '2018/9/22 17:27'

import ctypes
from collections import Iterable


class DynamicArray:
    def __init__(self, iterable=None):
        self._n = 0  # 实际元素个数
        self._capacity = 0  # 数组容量
        self._data = self._make_array(self._capacity)  # 底层数组容器
        if iterable is not None and not isinstance(iterable, Iterable):
            raise TypeError("'{}' object is not iterable".format(type(iterable)))
        elif iterable is not None:
            self.extend(iterable)

    def __len__(self):
        return self._n

    def __getitem__(self, i):
        if not 0 <= i < self._n:
            raise IndexError('invalid index')
        return self._data[i]

    def __setitem__(self, i, e):
        if not 0 <= i < self._n:
            raise IndexError('invalid index')
        self._data[i] = e

    def __repr__(self):
        s = ''
        for i in range(self._n):
            s += '{},'.format(self._data[i])
        return '[{}]'.format(s[:-1])

    def __contains__(self, e):
        for i in range(self._n):
            if e == self._data[i]:
                return True
        return False

    @property
    def capacity(self):
        return self._capacity

    def clear(self):
        self._n = 0
        self._capacity = 0
        self._data = self._make_array(self._capacity)

    def count(self, e):  # 返回元素e在数组中出现的次数
        i = 0
        for i in range(self._n):
            if self._data[i] == e:
                i += 1
        return i

    def extend(self, iterable):
        if not isinstance(iterable, Iterable):
            raise TypeError("'{}' object is not iterable".format(type(iterable)))
        for e in iterable:
            self.append(e)

    def index(self, e, start=None, end=None):  # 返回e在数组中首次出现的位置，[start, end)
        if start is None or start < 0:
            start = 0
        if end is None or end > self._n:
            end = self._n
        for i in range(start, end):
            if self._data[i] == e:
                break
        else:
            raise ValueError('{} not found'.format(e))
        return i

    def insert(self, i, e):
        if i < 0:
            i = 0
        elif i > self._n:
            i = self._n
        if self._n == self._capacity:  # 扩容
            self._resize(1 if self._capacity == 0 else 2 * self._capacity)
        for j in range(self._n, i, -1):  # i 的右边元素右移
            self._data[j] = self._data[j - 1]
        self._data[i] = e
        self._n += 1

    def append(self, e):
        if self._n == self._capacity:  # 扩容
            self._resize(1 if self._capacity == 0 else 2 * self._capacity)
        self._data[self._n] = e
        self._n += 1

    def pop(self, i=None):  # remove by index
        if i is None:
            i = self._n - 1
        if not 0 <= i < self._n:
            raise IndexError('pop index out of range')
        e = self._data[i]
        for i in range(i, self._n - 1):  # i 的右边元素左移
            self._data[i] = self._data[i + 1]
        self._data[self._n - 1] = None  # 断开引用，触发垃圾回收，节省空间
        self._n -= 1
        if self._n == self._capacity // 4:  # 1/4才缩容，防止抖动
            self._resize(self.capacity // 2)
        return e

    def remove(self, e):  # remove by element
        for i in range(self._n):
            if self._data[i] == e:
                self.pop(i)
                return
        raise ValueError('value not found')

    def reverse(self):  # 原地翻转数组
        for i in range(self._n // 2):
            self._data[i], self._data[self._n - i - 1] = self._data[self._n - i - 1], self._data[i]

    def _resize(self, new_size):
        new_array = self._make_array(new_size)
        for i in range(self._n):  # 复制数组内容
            new_array[i] = self._data[i]
        self._data = new_array  # 使用新的数组
        self._capacity = new_size

    def _make_array(self, capacity):
        return (capacity * ctypes.py_object)()  # 使用ctypes创建底层数组

__author__ = 'Hk4Fun'
__date__ = '2018/10/12 16:06'

from collections import defaultdict
import random
import time

test_func = []


def _swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def add_to_test(func):
    test_func.append(func)
    return func


@add_to_test
def bubble(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                _swap(arr, j, j + 1)


@add_to_test
def selection(arr):
    for i in range(len(arr)):
        minIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIdx]:
                minIdx = j
        _swap(arr, i, minIdx)


@add_to_test
def insertion(arr):
    for i, v in enumerate(arr):
        j = i - 1
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v


@add_to_test
def shell(arr):
    gap = len(arr) // 2
    while gap:
        for i, v in enumerate(arr):
            j = i - gap
            while j >= 0 and arr[j] > v:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = v
        gap //= 2


@add_to_test
def merge_u2d(arr):
    def merge(arr, aux, l, r):
        m = (l + r) // 2
        i, j = l, m + 1
        for k in range(l, r + 1):
            if i > m:
                aux[k] = arr[j]
                j += 1
            elif j > r:
                aux[k] = arr[i]
                i += 1
            elif arr[i] < arr[j]:
                aux[k] = arr[i]
                i += 1
            else:
                aux[k] = arr[j]
                j += 1

    def sort(arr, aux, l, r):
        if l < r:
            m = (l + r) // 2
            sort(aux, arr, l, m)
            sort(aux, arr, m + 1, r)
            merge(arr, aux, l, r)
            
    sort(arr[:], arr, 0, len(arr) - 1)


@add_to_test
def merge_d2u(arr):
    def merge(l, m, r):
        aux = arr[:]
        i, j = l, m + 1
        for k in range(l, r + 1):
            if i > m:
                arr[k] = aux[j]
                j += 1
            elif j > r:
                arr[k] = aux[i]
                i += 1
            elif aux[i] < aux[j]:
                arr[k] = aux[i]
                i += 1
            else:
                arr[k] = aux[j]
                j += 1

    sz = 1
    while sz < len(arr):
        for l in range(0, len(arr) - sz, 2 * sz):
            merge(l, l + sz - 1, min(l + 2 * sz - 1, len(arr) - 1))
        sz *= 2


@add_to_test
def quick(arr):
    def partition(l, r):
        pivot = arr[l]
        while l < r:
            while l < r and arr[r] >= pivot: r -= 1
            arr[l] = arr[r]
            while l < r and arr[l] < pivot: l += 1
            arr[r] = arr[l]
        arr[l] = pivot
        return l

    def sort(l, r):
        if l < r:
            idx = partition(l, r)
            sort(l, idx - 1)
            sort(idx + 1, r)

    sort(0, len(arr) - 1)


@add_to_test
def quick_3way(arr):
    def partition(l, r):
        pivot = arr[l]
        lt, gt = l, r
        i = l + 1
        while i <= gt:
            if arr[i] < pivot:
                _swap(arr, lt, i)
                i += 1
                lt += 1
            elif arr[i] > pivot:
                _swap(arr, gt, i)
                gt -= 1
            else:
                i += 1
        return lt, gt

    def sort(l, r):
        if l < r:
            lt, gt = partition(l, r)
            sort(l, lt - 1)
            sort(gt + 1, r)

    sort(0, len(arr) - 1)


@add_to_test
def heap_max(arr):
    def sink(i, end):
        while True:
            l, r = 2 * i + 1, 2 * i + 2
            largest = i
            if l < end and arr[l] > arr[largest]:
                largest = l
            if r < end and arr[r] > arr[largest]:
                largest = r
            if largest == i: break
            _swap(arr, i, largest)
            i = largest

    for i in range(len(arr) // 2, -1, -1):
        sink(i, len(arr))
    for end in range(len(arr) - 1, -1, -1):
        _swap(arr, 0, end)
        sink(0, end)


def test_sort(func):
    arr = raw_arr[:]  # 由于所有排序算法原地排序，因此做一份拷贝
    start = time.time()
    func(arr)
    end = time.time()
    try:
        assert arr == res
    except AssertionError:
        print(func.__name__, '!!!AssertionError!!!')
        print('result: {}'.format(arr))
        print('expected: {}'.format(res))
    test_time[func.__name__].append(end - start)


if __name__ == '__main__':
    ARR_LEN = 200  # 数组长度
    NUM_LIMIT = 100  # 数字范围：[0, NUM_LIMIT]
    TEST_NUM = 100  # 测试次数
    test_time = defaultdict(list)
    for _ in range(TEST_NUM):
        raw_arr = [random.randint(0, NUM_LIMIT) for _ in range(ARR_LEN)]
        res = sorted(raw_arr)  # sorted 不是原地排序，而是返回有序数组
        for func in test_func:
            test_sort(func)
    for item in sorted(test_time.items(), key=lambda item: sum(item[1])):
        print('{}: {:.2f} ms'.format(item[0], sum(item[1]) * 1000 / len(item[1])))

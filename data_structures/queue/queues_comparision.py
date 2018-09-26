__author__ = 'Hk4Fun'
__date__ = '2018/9/24 19:30'

import time

from array_queue import ArrayQueue
from loop_queue import LoopQueue
from array_deque import ArrayDeque
from loop_deque import LoopDeque

TEST_NUM = 10000


def queue_exec_time(queue):
    start = time.time()

    for i in range(TEST_NUM):
        queue.enqueue(i)

    for i in range(TEST_NUM):
        queue.dequeue()

    end = time.time()

    return end - start


def deque_exec_time(deque):
    start = time.time()

    for i in range(TEST_NUM // 2):
        deque.push_tail(i)

    for i in range(TEST_NUM // 2):
        deque.push_front(i)

    for i in range(TEST_NUM // 2):
        deque.pop_tail()

    for i in range(TEST_NUM // 2):
        deque.pop_front()

    end = time.time()

    return end - start


if __name__ == '__main__':
    queue = ArrayQueue(TEST_NUM)
    print('ArrayQueue, time: {}'.format(queue_exec_time(queue)))
    queue = LoopQueue(TEST_NUM)
    print('LoopQueue, time: {}'.format(queue_exec_time(queue)))
    deque = ArrayDeque(TEST_NUM)
    print('ArrayDeque, time: {}'.format(deque_exec_time(deque)))
    deque = LoopDeque(TEST_NUM)
    print('LoopDeque, time: {}'.format(deque_exec_time(deque)))

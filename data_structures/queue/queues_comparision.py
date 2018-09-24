__author__ = 'Hk4Fun'
__date__ = '2018/9/24 19:30'

import time

from array_queue import ArrayQueue
from loop_queue import LoopQueue

TEST_NUM = 10000


def exec_time(queue):
    start = time.time()

    for i in range(TEST_NUM):
        queue.enqueue(i)

    for i in range(TEST_NUM):
        queue.dequeue()

    end = time.time()

    return end - start


if __name__ == '__main__':
    queue = ArrayQueue(TEST_NUM)
    print('ArrayQueue, time: {}'.format(exec_time(queue)))
    queue = LoopQueue(TEST_NUM)
    print('LoopQueue, time: {}'.format(exec_time(queue)))

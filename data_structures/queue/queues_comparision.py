__author__ = 'Hk4Fun'
__date__ = '2018/9/24 19:30'

import time

from array_queue import ArrayQueue
from array_deque import ArrayDeque
from array_loop_queue import ArrayLoopQueue
from array_loop_deque import ArrayLoopDeque
from linked_list_queue import LinkedListQueue
from linked_list_deque import LinkedListDeque
from linked_list_loop_queue import LinkedListLoopQueue
from linked_list_loop_deque import LinkedListLoopDeque

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
    print('TEST_NUM: {}'.format(TEST_NUM))

    queue = ArrayQueue(TEST_NUM)
    print('ArrayQueue, time: {:.3f} s'.format(queue_exec_time(queue)))

    queue = LinkedListQueue(TEST_NUM)
    print('LinkedListQueue, time: {:.3f} s'.format(queue_exec_time(queue)))

    queue = ArrayLoopQueue(TEST_NUM)
    print('ArrayLoopQueue, time: {:.3f} s'.format(queue_exec_time(queue)))

    queue = LinkedListLoopQueue(TEST_NUM)
    print('LinkedListLoopQueue, time: {:.3f} s'.format(queue_exec_time(queue)))

    deque = ArrayDeque(TEST_NUM)
    print('ArrayDeque, time: {:.3f} s'.format(deque_exec_time(deque)))

    deque = LinkedListDeque(TEST_NUM)
    print('LinkedListDeque, time: {:.3f} s'.format(deque_exec_time(deque)))

    deque = ArrayLoopDeque(TEST_NUM)
    print('ArrayLoopDeque, time: {:.3f} s'.format(deque_exec_time(deque)))

    deque = LinkedListLoopDeque(TEST_NUM)
    print('LinkedListLoopDeque, time: {:.3f} s'.format(deque_exec_time(deque)))

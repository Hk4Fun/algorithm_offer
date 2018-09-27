__author__ = 'Hk4Fun'
__date__ = '2018/9/28 1:44'

import time

from array_stack import ArrayStack
from linked_list_stack import LinkedListStack

TEST_NUM = 10000


def stack_exec_time(stack):
    start = time.time()

    for i in range(TEST_NUM):
        stack.push(i)

    for i in range(TEST_NUM):
        stack.pop()

    end = time.time()

    return end - start


if __name__ == '__main__':
    stack = ArrayStack()
    print('ArrayStack, time: {} s'.format(stack_exec_time(stack)))
    stack = LinkedListStack()
    print('LinkedListStack, time: {} s'.format(stack_exec_time(stack)))

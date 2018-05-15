__author__ = 'Hk4Fun'
__date__ = '2018/5/16 1:50'
'''题目描述：
Implement the following operations of a stack using queues.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
empty() -- Return whether the stack is empty.

Notes:
You must use only standard operations of a queue -- 
which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. 
You may simulate a queue by using a list or deque (double-ended queue), 
as long as you use only standard operations of a queue.
You may assume that all operations are valid 
(for example, no pop or top operations will be called on an empty stack).
'''
'''主要思路：

'''


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        if self.queue1:
            self.queue1.append(x)
        else:
            self.queue2.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.queue1:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop(0)
        else:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop(0)

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.queue1:
            for i in range(len(self.queue1) - 1):
                self.queue2.append(self.queue1.pop(0))
            top = self.queue1[0]
            self.queue2.append(self.queue1.pop(0))
            return top
        else:
            for i in range(len(self.queue2) - 1):
                self.queue1.append(self.queue2.pop(0))
            top = self.queue2[0]
            self.queue1.append(self.queue2.pop(0))
            return top

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.queue1 and not self.queue2: return True
        return False

__author__ = 'Hk4Fun'
__date__ = '2018/5/15 23:53'
'''题目描述：
Design a stack that supports push, pop, top, 
and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
'''
'''主要思路：
target_offer/21_包含min函数的栈.py
空间O（n），所有操作时间O（1）
'''


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack, self.minStack = [], []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if not self.minStack or self.getMin() > x:
            self.minStack.append(x)
        else:
            self.minStack.append(self.getMin())

    def pop(self) -> None:
        if not self.stack: return
        self.minStack.pop()
        return self.stack.pop()

    def top(self) -> int:
        if not self.stack: return
        return self.stack[-1]

    def getMin(self) -> int:
        if not self.minStack: return
        return self.minStack[-1]

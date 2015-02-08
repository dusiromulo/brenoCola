__author__ = 'Roland'


class Stack():

    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, element):
        if not len(self.stack) == self.size - 1:
            self.stack.append(element)

    def pop(self):
        element = self.stack[0]
        self.stack = self.stack[1:]
        return element